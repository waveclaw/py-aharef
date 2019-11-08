#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 see http://www.aharef.info/static/htmlgraph/?url=
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : GhettoDrawer.py
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
from pyaharef.globals import X, Y, ANGLE, polar2rectangular

from . import tree
# Math function for conversions
from math import exp


class Ghetto(tree.Tree):
    """
     No real physics?  No problem!
        1. draw fixed length line
        2. have children draw at fixed location
        3. draw the icon
    """

    def endpoint(self, child, style, depth):
        """
        Use fixed angles based on the fixed length globals
        but reset the length based on a decay function
        :type child: object
        :type style: object
        :type depth: int
        """
        angle = (style.count / 3.14) * style.position * \
                (exp(depth) + 1 / exp(depth)) + style.start[ANGLE]
        length = self.size / (2 * (depth + 1))
        '''
        if length > DEFAULT_LENGTH:
            # decay as 1/X but increase by # of children
            length = self.size / (length * exp(depth))
        '''
        end = (style.start[X] +
               polar2rectangular(length, angle)[X],
               style.start[Y] +
               polar2rectangular(length, angle)[Y],
               angle)
        print(f'returning end of {end} in location {style.position}, for {style.count} children')
        return end
