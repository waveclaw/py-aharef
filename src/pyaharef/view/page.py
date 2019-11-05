#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 see http://www.aharef.info/static/htmlgraph/?url=
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : PageType.py
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
############################################################################
"""
from ../globals import DOT_COLOR, DEFAULT_COLOR, \
    DEFAULT_HEIGHT, DEFAULT_WIDTH, X, Y
from ../style import Style
from . import tree.Tree as Tree


class Page(Tree):
    """
    draw a page
    """

    def style(self, tree, style, position):
        try:
            color = DOT_COLOR[tree.tag]
        except KeyError, err:
            print 'No color defined for', tree.tag, str(err)
            color = DEFAULT_COLOR
        return Style.Style(color=color,
                           start=style.start,
                           position=position,
                           count=style.count)

    def icon(self, style=None, end=None):
        """
        Draw a dot for the root
        """
        self.graph.create_oval(end[X] - DEFAULT_HEIGHT,
                               end[Y] - DEFAULT_WIDTH,
                               end[X] + DEFAULT_HEIGHT,
                               end[Y] + DEFAULT_WIDTH,
                               fill=style.color,
                               tags=style.gettag() + 'icon')
        # even faster than destroy for clearing the screen. D'oh!
        # scalefactor = ( max(X,Y)  / length )
        # self.graph.scale('scale', 0, 0, scalefactor, scalefactor)
        if self.iconaction:
            self.iconaction(style, end)


    def stem(self, end=None, style=None):
        """
        Draw the stem
        """
        # draw line
        self.graph.create_line(style.start[X], style.start[Y],
                               end[X], end[Y],
                               # width = style.width,
                               tags=style.gettag() + 'stem')
