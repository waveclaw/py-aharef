#!/usr/bin/python
"""
 see http://www.aharef.info/static/htmlgraph/?url=
############################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : pyaharef/globals.py
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
from math import cos, sin, hypot, atan2

# globals
GRAPH_TYPE = [(0, 'Document'), (1, 'Site')]
DEFAULT_URL = 'Type in a url like file:// or http://'
DEFAULT_WIDTH = 5
DEFAULT_HEIGHT = 5
DEFAULT_COLOR = 'gray90'
DEFAULT_LENGTH = 15

DOT_COLOR = {'a': 'yellow', 'link': 'yellow', 'p': 'purple', 'html': 'blue', 'br': 'brown', 'em': 'red',
             'pre': '#EFDECD', 'head': 'violet', 'div': 'green', 'span': '#8B008B', 'form': '#654321',
             'input': '#4D5D53', 'img': 'black', 'tt': '#00FFFF', 'hr': '#C2B280', 'dt': '#B5A642', 'dd': '#734F96',
             'dl': '#FF007F', 'ul': '#F5F5DC', 'ol': '#FFE4C4', 'li': '#007BA7', 'table': 'orange', 'td': '#7B3F00',
             'tr': '#C19A6B', 'col': '#B06500', 'th': '#CC6666', 'meta': '#36454F', 'title': '#D2691E', 'h1': '#00FF7F',
             'h2': '#ADFF2F', 'h3': '#66B032', 'h4': '#008000', 'h5': '#A8E4A0', 'body': '#00008B'}  # Darkblue

# For Pymunk
FRAME_RATE = 30
SPACE_RATE = 50.0  # float
COULOMB_FORCE = 8.987551787e9

# Convenience Numbers
X = 0
Y = 1
ANGLE = 2  # yes, position in this game is a trit!

# For Ghetto


def polar2rectangular(length, angle):
    """
    from 0,0 give radian, length -> x, y
    """
    return length * cos(angle), length * sin(angle)


def rectangular2polar(xcoord, ycoord):
    """
    from 0,0 give x,y -> radian, length
    """
    return hypot(xcoord, ycoord), atan2(ycoord, xcoord)


if __name__ == '__main__':
    print 'Globals for pyaharef'
