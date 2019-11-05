#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 see http://www.aharef.info/2006/05/websites_as_graphs.htm
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : TreeType.py
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


class Tree:
    """
    What thing to you want to draw?
    """
    def __init__(self, graph, size = 0, iconaction=None):
        self.graph = graph
        self.size = size
        self.iconaction = iconaction

    def style(self, tree, style, position):
        """
        Determine what style to use
        """
        pass

    def stem(self, end, style):
        """
        Draw the stem
        """
        pass

    def icon(self, style = None, end = None):
        """
        Draw the icon
        """
        # this is the extra callback needed for adding Pymunk objects
        if self.iconaction:
            self.iconaction(style, end)
