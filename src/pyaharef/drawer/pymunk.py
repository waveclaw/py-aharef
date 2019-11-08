#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 see http://www.aharef.info/static/htmlgraph/?url=
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : PymunkDrawer.py
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
 23-SEP-2011  0.4/0.6        SHELL001 jdpowell Split out modules
 05-NOV-2019  0.6/0.7        PYTHN001 jdpowell Create a GitHub project
############################################################################

"""
from . import tree
import pymunk
from ChargedBody import ChargeBody # typo, will fail

def movethings(graph, updatelist):
    for (tag, thing) in self.updatelist:
        if tag and thing:
            # find out if root(tag) moved, update start of stem
            #move end of self.graph(tag + 'stem', thing.loc)
            #
            # move self.graph(tag + 'icon', thing.loc)
            pass

def pymunk_after(space = None, graph = None, updatelist = None):
    '''
   process the world
    ... pymunk funcs ...
   update the canvas
      ... graph.moves() ...
   let the real mainloop() worry about details
    see http://kmkeen.com/mainloops/ and
    http://infohost.nmt.edu/tcc/help/pubs/tkinter/universal.html
    '''
    milliseconds = int(round(1000.0 / FRAME_RATE))
    #  Right now, there is nothing redrawing the damn screen,
    #  need to wipe the graph and somehow re-invoke the draw methods
    if space:
        space.step(1/ SPACE_RATE) # constant from pymunk
        # movethings()

    graph.after(milliseconds,
                lambda:pymunk_after(space = space,
                                    graph = graph,
                                    updatelist = updatelist))

class Pymunk(tree.Tree):
    '''
     Pseudo-real physics using chipmunk via pymunk.
     Needs a Charged body implementation ala
     the chipmunk MagnetsElectric.c demo
    '''
    def __init__(self, tree = None, graph = None, drawertype = None):
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 0.0) # freely floating
        self.updatelist = []
        self.position = ( self.graph.winfo_reqwidth() / 2,
                self.graph.winfo_reqheight() / 2 )
        TreeDrawer.__init__(self, tree, graph, type)
        self.drawertype.gettags = self.gettags
        # hooks for the physics model
        self.graph.after(1,
            lambda:pymunk_after(space = self.space,
                                graph = self.graph,
                                updatelist = self.updatelist)
                         )
        if type:
            # replace with one tied to this PymunkTree
            type.iconaction = self.addtospace

    def endpoint(self, child, style, depth):
        '''
        figure out my destination
        this works with pymunk_after and addtospace
        to push children away from the root
        '''
        # add object to space
        # thing = self.addtospace(style.gettag())
        # add reference to tracking list (graph tag, object)
        # self.updatelist.append((tag, thing)) <<--- needs to be a tree structure!
        # simulate 1 step
        #  self.pymunk_after()
        # walk list doing moves
        #  self.movethings()
        pass

    def addtospace(self, tag):
        '''
        Do the normal icon output, but also
        add a physical object to the model
        '''
        pass
        #return self.space.addbody()
