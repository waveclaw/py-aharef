#!/usr/bin/python
"""
 see http://www.aharef.info/static/htmlgraph/?url=
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : pyaharef/style.py
 CREATED     : 26-APR-2011 JDPOWELL
 DESCRIPTION : global settings for the application, mostly constants
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

from globals import DEFAULT_COLOR, X, Y

class Style:
    """
    new-style class-ified tuple to get around having huge
    numbers of options on some of the methods

    This is the 'helper' object passed between Tree Views & Tree Drawers
    to abstract the notion of the drawn thing, addressing that drawn
    thing and it's properties.

    Possible alternative is to decorate the ElementTree values, but
    then the case of switching from Pages to Site view becomes an issue.
    """
    def __init__(self, color, position, start, count):
        """
        Enable defaults to be set or overridden
        """
        self.color = None   # color from table
        self.position = 0   # which index in count siblings
        self.count = 0      # number of siblings
        self.start = (0, 0, 0) # root position
        # synthetic properties
        # length, width,
        self.setproperties(color, position, start, count)

    def getproperties(self):
        """
        annoying function to shut up pylint
        """
        return self.color, self.position, self.start, self.count

    def setproperties(self, color=DEFAULT_COLOR, position=0, start=None, count=0):
        """
        another annoying function
        :type self: object
        :type position: object
        """
        self.color = color
        self.position = position
        self.count = count
        if not start:
            self.start = (0, 0, 0)
        else:
            self.start = start

    def gettag(self, depth=0):
        """
        tag for use with pymunk
        """
        tag = ''
        assert isinstance(self.color, object)
        for aspect in [self.color, self.start[X], self.start[Y], depth, self.count, self.position]:
            tag += str(aspect)
        return tag
