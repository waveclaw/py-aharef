#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 see http://www.aharef.info/2006/05/websites_as_graphs.htm
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
 05-NOV-2019  0.6/0.7        PYTHN001 jdpowell Create a GitHub project
 05-NOV-2019  0.6/0.7        PYTHN001 jdpowell Create a GitHub project
############################################################################

"""
# parsing tools
import urllib2
from elementtree import ElementTree


class Tree():
    """
    DocumentParsers will be either siteWalkers or BeautifulSoup parsers
    This class only manages getting a handle on the file
    """

    def __init__(self, document=None):
        self.document = document

    @property
    def parse(self):
        """
        open the root URL and go there, walk whatever is there and return a tree
        """
        # do _walk here
        # print 'getting', self.document
        url = urllib2.Request(self.document)
        try:
            response = urllib2.urlopen(url)
        except urllib2.URLError, err:
            raise err
        tree = None
        if response:
            tree = self.walk(response)
        if not tree:
            tree = ElementTree.Element("root")
        return tree

    def walk(self, response=None):
        """
        parse a document to product a tag tree. Required to be overloaded
        :rtype : object
        :param response:
        """
        pass


if __name__ == '__main__':
    print 'pyaharef: treeparser'
    print(str(Tree()))
