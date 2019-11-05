#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 see http://www.aharef.info/static/htmlgraph/?url=
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : pyaharef/graphgui
 CREATED     : 26-APR-2011 JDPOWELL
 DESCRIPTION : parse a webpage, display as a graph
 ASSUMPTIONS : Familiarity with HTTP, Python, urllib2, BeautifulSoup
############################################################################
                          RELEASE LICENSE

   This file is available under copyright  2011 Jeremiah D. Powell.
   For internal use only,
   keep out of young children.

   Copyrights to their respective owners.

  Current version : $Ver:0.2$
  Latest version  : 0.1
  Bugs, Comments  : waveclaw@waveclaw.net
############################################################################
                          RELEVANT DOCUMENTS
                           (REFERENCES)

  Name                            Comment
  ------------------------------- -------------------------------------

############################################################################
                          REVISION HISTORY
 Date         Version(Build) SCM      Engineer Comment/Description
 DD-MMM-YYYY  Rel.Patch.Pnt  Reason
 -----------  -------------- -------- -------- -------------------------
 26-APR-2011  0.1/0.1(1)     WWW00661 jdpowell Copied from other scripts
############################################################################

"""
# Tkinter, the portable GUI
from Tkconstants import N, S, E, W, \
    X, LEFT, RIGHT, BOTH, SUNKEN, YES, \
    TOP, BOTTOM, ALL
from Tkinter import Frame, Canvas, IntVar, Radiobutton, Label, Button
# Tix, the Tkinter extensions
import Tix
# pyahref internals
from globals import DEFAULT_URL, GRAPH_TYPE
from parser import document, site, tree
from view import page, site

try:
    from drawer.Pymunk import Drawer as myTreeDrawer
except ImportError:
    print 'Using Ghetto Drawer, could not import PymunkDrawer'
    from drawer.ghetto import Drawer as myTreeDrawer

PARSERS = [document.Document, site.Site]
VIEWTYPE = [page.Page, site.Site]


class Gui():
    """
   This the class that defines the GUI parts outside the
   graphics area and manages the behavior of these controls
    """

    def __init__(self, parent=None, url=DEFAULT_URL, **args):
        """
        Setup the placeholders
        :type parent: object
        :type url: String
        """
        self.parentframe = Frame(parent, args)
        self.urls = [url]
        self.urlbar = None
        self.graphtype = IntVar()
        self.graph = None
        self.status = None
        self.pack()
        self.drawgraph()

    def pack(self):
        """
        Layout the GUI
        """
        self.parentframe.pack(side=LEFT, fill=BOTH, expand=YES)
        topframe = Frame(self.parentframe)
        # self.urlbar = Text(topframe, bg = '#FFFFFF', width = 64, height = 1)
        self.urlbar = Tix.ComboBox(topframe, bg='#FFFFFF',
                                   editable=True, variable=self.urls,
                                   command=lambda x: self.drawgraph())
        if self.urls[0]:
            self.urlbar['selection'] = self.urls[0]
        else:
            self.urlbar['selection'] = DEFAULT_URL
        self.urlbar.pack(side=LEFT, anchor=E, fill=X, expand=YES)
        Button(topframe,
               text='Go To',
               anchor=E,
               command=self.drawgraph).pack(side=LEFT)
        radioframe = Frame(topframe)
        for (index, name) in GRAPH_TYPE:
            radiobutton = Radiobutton(radioframe,
                                      text=name,
                                      value=index,
                                      variable=self.graphtype)
            radiobutton.pack(side=TOP, anchor=W, expand=YES)
        radioframe.pack(side=RIGHT, anchor=W, expand=YES)
        topframe.pack(side=TOP, anchor=W, expand=YES, fill=X)
        bottomframe = Frame(self.parentframe)
        self.graph = Canvas(bottomframe,
                            bg='#FFFFFF',
                            height=600,
                            width=600)
        self.graph.pack(fill=BOTH, anchor=N, expand=YES)
        bottomframe.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.status = Label(bottomframe,
                            text=self.urls[0],
                            bd=1,
                            relief=SUNKEN,
                            anchor=W)
        self.status.pack(side=BOTTOM,
                         anchor=S,
                         fill=X,
                         expand=YES)

    def drawgraph(self):
        """
        Re-draw the graphical area, update the url list and status line to match
        """
        assert isinstance(self.urlbar, object)
        text = self.urlbar['selection']
        if '' == text:
            return
        if text != DEFAULT_URL:
            # be consistent and update the history
            self.urlbar.insert(Tix.END, text)
        if text and text != "\n" and text not in self.urls:
            self.urls.append(text)
        # print self.urls
        if text and text != '\n':
            statustext = text
        else:
            statustext = 'nowhere in particular.'
        # select parser based on self.radioButtons
        # where the view type has to match the parser type
        (index, name) = GRAPH_TYPE[self.graphtype.get()]
        maketree = PARSERS[index](document=text)
        view = VIEWTYPE[index]
        print 'Parser is', str(maketree)
        print 'View is', str(view), 'called', name
        if statustext == DEFAULT_URL:
            self.status['text'] = statustext
            return
        else:
            self.status['text'] = ' '.join(("Graphing",
                                            name,
                                            "at",
                                            statustext))
        try:
            self.graph.delete(ALL)
            # Might optimize to not re-parse a parsed tree,
            # cache the tree and check if the current text from urlbar
            #  is same as old then kick off draw.
            # But then you have to deal with if the url has expired.
            documenttree = maketree.parse
            treedrawer = myTreeDrawer(graph=self.graph,
                                      tree=documenttree,
                                      drawertype=view)
            print 'Drawer is', str(treedrawer)
            treedrawer.draw()
        except Exception, err:
            if hasattr(err, 'reason'):
                self.status['text'] = ''.join(('Failed to reach url: ',
                                               str(err.reason)))
            elif hasattr(err, 'code'):
                self.status['text'] = ''.join(('Error code: ', str(err.code)))
            else:
                self.status['text'] = 'Some error happened displaying your URL.'
                print "Exception", str(err)
            raise err


if __name__ == '__main__':
    print 'Graphics GUI testing goes here.'
    ROOT_WINDOW = Tix.Tk()  # not Tk, need the combo box widget
    ROOT_WINDOW.wm_title('PyAharef: GraphGUI')
    GUI = Gui(parent=ROOT_WINDOW)
    ROOT_WINDOW.pack()
    ROOT_WINDOW.mainloop()
