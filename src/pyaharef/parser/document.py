#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 see http://www.aharef.info/static/htmlgraph/?url=
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : Document.py
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

from tree import Tree
from ../elementsoup import ElementSoup

class Document(Tree):
    """
    Specialized parser that returns an ElemenTree
    that knows what color and tags are in each element
    """

    def walk(self, response=None):
        """
        Walk a page, returning elements
        """
        #page =  response.read()
        #cleanedPage = BeautifulSoup(response).prettify()
        if response:
            #tree = ElementTree.parse(cleanedPage).getroot()
            tree = ElementSoup.parse(response)
        return tree
