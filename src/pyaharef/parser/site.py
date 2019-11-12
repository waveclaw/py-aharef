#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 see http://www.aharef.info/2006/05/websites_as_graphs.htm
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : DocumentParser.py
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
from pyaharef.parser.tree import Tree
from pyaharef.sitewalker import SiteWalker
from xml.etree.ElementTree import ElementTree
from bs4 import BeautifulSoup, SoupStrainer
import re

DOCUMENT = re.compile('.*[.](?!html|htm|aspx|pl|php|asp|/).*$',
                      re.IGNORECASE)
MEDIA = re.compile('.*[.](?!png|jpe*g|fmv|mlv|gif|svg|img|bmp|ogg|mp3)$',
                   re.IGNORECASE)


def findurls(openedpage):
    """
    find the page's urls
    """
    newurls = []
    try:
        newurls.extend([tag['href'] for tag in
                        BeautifulSoup(openedpage,
                                      parseOnlyThese=SoupStrainer('a'))
                        if tag.has_key('href')])
    except (ValueError, KeyError):
        print("tag without href")
    return newurls


def gettype(url):
    """
    What kind of thing is at this url?
    """
    if DOCUMENT.match(url):
        return 'document'
    if MEDIA.match(url):
        return 'media'
    return 'url'


class _site_visitor:
    """
    helper class for SiteParser
    """

    def __init__(self, url=None):
        """
         take url
         start an ElementTree with it
        """
        if url and '' != url:
            self.root = ElementTree.Element(gettype(url))
            self.root.text = url

    def visit(self, page=None):
        """
        Add the current page with
        all the urls in it descending from it
        """
        if page:
            url = page.geturl()
            urltype = gettype(url)
            scanner = self.root.getiterator(urltype)
            for loc in scanner:
                if loc.text == url:
                    location = loc
            if location:
                pass
            else:
                location = ElementTree.SubElement(self.root, urltype)
                location.text = url
            for link in findurls(page):
                subelement = ElementTree.SubElement(location, gettype(link))
                assert isinstance(subelement, object)
                subelement.text = link

    def getroot(self):
        """
        Return the root of the tree
        """
        return self.root


class Site(Tree):
    """
    Specialized parser that returns an ElemenTree
    that knows what icons to use for a site
    """

    def walk(self, response=None):
        """
        Walk a tree of links
        In future, return each file type and follow img and script links
        """

        if response:
            # prime the pump
            sitevisitor = _site_visitor(response.geturl())
            sitevisitor.visit(response)
            # walk the site
            walker = SiteWalker(self.document)
            walker.walk(visitor=sitevisitor)
            return sitevisitor.getroot()
        else:
            return None
