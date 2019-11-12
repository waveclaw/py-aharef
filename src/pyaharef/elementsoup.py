#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 element loader based on BeautifulSoup
 see http://www.crummy.com/software/BeautifulSoup/
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Leonard Richardson
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : elementsoup.py
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
from bs4 import BeautifulSoup as BS
from bs4 import Comment, Declaration, ProcessingInstruction

# soup classes that are left out of the tree
ignorable_soup = [ Comment, Declaration, ProcessingInstruction ]

# slightly silly
try:
    import xml.etree.cElementTree as ET
except ImportError:
    try:
        import cElementTree as ET
    except ImportError:
        import elementtree.ElementTree as ET

import html, re

pattern = re.compile("&(\w+);")

name2codepoint = html.entities.name2codepoint


def unescape(string):
    """
     work around oddities in BeautifulSoup's entity handling
    :param string:
    :return:
    """

    def unescape_entity(m):
        try:
            return unichr(name2codepoint[m.group(1)])
        except KeyError:
            return m.group(0)  # use as is

    return pattern.sub(unescape_entity, string)


def parse(afile, builder=None, encoding=None):
    """
    Load an XHTML or HTML file into an Element structure, using Leonard
    Richardson's tolerant BeautifulSoup parser.

    :rtype : object
    :param afile: File-like Object to process
    :param builder: Optional tree builder.  If omitted, defaults to the
     "best" available <b>TreeBuilder</b> implementation.
    :param encoding: encoding of the data in the input file.
    :return: An Element instance representing the HTML root element.
    """
    bob = builder

    def emit(this_soup):
        """
        emit cleaned up html
        :type this_soup:
        """
        if isinstance(this_soup, BS.element.NavigableString):
            for ignorable in ignorable_soup:
              if isinstance(this_soup, ignorable):
                return
            bob.data(unescape(this_soup))
        else:
            attrib = dict([(k, unescape(v)) for k, v in this_soup.attrs])
            bob.start(this_soup.name, attrib)
            for s in this_soup:
                emit(s)
            bob.end(this_soup.name)

    # determine encoding (the document charset is not reliable)
    if not hasattr(afile, "read"):
        infile = open(afile)
    text = infile.read()
    assert isinstance(encoding, object)
    if not encoding:
        try:
            encoding = "utf-8"
            unicode(text, encoding)
        except UnicodeError:
            encoding = "iso-8859-1"
    soup = BS.BeautifulSoup(
        text, convertEntities="html", fromEncoding=encoding
    )
    # build the tree
    if not bob:
        bob = ET.TreeBuilder()
    emit(soup)
    root = bob.close()
    assert isinstance(root, object)
    # wrap the document in a html root element, if necessary
    if 1 == len(root) and "html" == root[0].tag:
        return root[0]
    root.tag = "html"
    return root


if __name__ == "__main__":
    import sys

    source = sys.argv[1]
    if source.startswith("http:"):
        import urllib
        source = urllib.request.urlopen(source)
    print(ET.tostring(parse(source)))
