#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 see http://www.aharef.info/static/htmlgraph/?url=
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : pyaharef
 CREATED     : 26-APR-2011 JDPOWELL
 DESCRIPTION : parse a webpage, display as a graph
 ASSUMPTIONS : Familiarity with HTTP, Python, urllib2, BeautifulSoup
############################################################################
                          RELEASE LICENSE

   This file is available under copyright  2011 Jeremiah D. Powell.
   For internal use only, keep out of young children.
   This is not underwear, do not put inside of your pants.

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
 11-JUN-2011  0.2/0.2(0)     WWW00661 jdpowell Working minimal copy
 25-JUL-2011  0.3/0.3(0)     WWW00661 jdpowell Refactor heavily
 05-NOV-2019  0.6/0.7        PYTHN001 jdpowell Create a GitHub project
############################################################################

"""

# pyahref internals
from ../globals import X, Y, DEFAULT_COLOR
from ../Style import Style
# Pymunk is conditionally imported bellow to pick which subclass to use
# import pymunk


class Tree:
    """
    Draw the tree on a Tkinter canvas object or something that has the
    same API as canvas

    The tree to draw needs to implement parts of the ElementTree API
    """

    def __init__(self, tree=None, graph=None, drawertype=None):
        """
        New TreeDrawer attached to a Tk Canvas object
        """
        self.tree = tree
        self.graph = graph
        self.size = self.getsize
        self.drawertype = drawertype(graph=graph, size=self.size)

    def iterparent(self):
        """
        The following is from http://effbot.org/zone/element.htm
        iterator which gives (parent, child) tuples
        """
        for parent in self.tree.getiterator():
            for child in parent:
                yield parent, child

    @property
    def getparents(self):
        """
         The following is from http://effbot.org/zone/element.htm
        Return a new data structure that maps each child to it's parent
        """
        return dict((c, p) for p in self.tree.getiterator() for c in p)

    @property
    def getsize(self):
        """
        Given a tree, find the length of the max parent path
        """
        depth = 0
        if self.tree:
            parentlist = self.getparents
            root = self.tree
            for child in self.tree.getiterator():
                count = 1
                cnow = child
                # follow parentlist[c], counting as we go
                while cnow is not root:
                    cnow = parentlist[cnow]
                    count += 1
                if count > depth:
                    depth = count
        return depth

    def endpoint(self, child, style, depth):
        """
        figure out my destination
        :type child: object
        :type style: object
        :type depth: int
        """
        pass

    def draw(self, child=None, style=None, depth=0):
        """
         How to actually draw on the canvas is handled by subclasses
        :type self: object
        """
        if not self.graph or not self.tree:
            return
        if not child:
            # root case, figure it out ourselves
            end = (self.graph.winfo_reqwidth() / 2,
                   self.graph.winfo_reqheight() / 2,
                   0)  # no angle
            self.size = max(end[X], end[Y])
            print 'Drawing a tree with root', self.tree,
            print  'of size', self.size
            mystyle = Style(color=DEFAULT_COLOR,
                            position=0,
                            count=0,
                            start=end)
            children = self.tree.getchildren()
            mystyle.count = len(children)
            # pass it through the drawertype to pickup the color
            mystyle = self.drawertype.style(tree=self.tree,
                                            style=mystyle,
                                            position=0)
            print 'root"s', children, 'from', mystyle.start, 'to', end
        else:
            mystyle = style
            children = child.getchildren()
            end = self.endpoint(child, style, depth)
        # draw the root element and all subtree
        self.drawertype.stem(end=end, style=mystyle)
        childpos = 0
        for mychild in children:
            if mychild:  # possible iteraion on null due to Element
                mychildstyle = self.drawertype.style(tree=mychild,
                                                     style=mystyle,
                                                     position=childpos)
                mychildstyle.start = end
                mychildstyle.count = mystyle.count
                print 'my child', mychild, 'at', end
                self.draw(child=mychild,
                          style=mychildstyle,
                          depth=depth + 1)
                childpos += 1
        self.drawertype.icon(end=end, style=mystyle)


if __name__ == '__main__':
    print 'pyaharef: treedrawer'
    TREE = TreeDrawer()
    print(str(TREE))
