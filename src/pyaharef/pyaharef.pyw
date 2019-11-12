#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 see http://www.aharef.info/2006/05/websites_as_graphs.htm
########################################################################
 TITLE       : Webiste as Graph
 PROJECT     : www
 ENGINEER    : Jeremiah D. Powell
 PROGRAM     : aharef Website grapher using Tkinter libs
 FILE        : pyaharef
 CREATED     : 26-APR-2011 JDPOWELL
 DESCRIPTION : parse a webpage, display as a graph
 ASSUMPTIONS : Familiarity with HTTP, Python, urllib2, BeautifulSoup
########################################################################
                          RELEASE LICENSE

   This file is available under copyright  2011 Jeremiah D. Powell.
   For internal use only,
   keep out of young children.

   Copyrights to their respective owners.

  Current version : $Ver:0.2$
  Latest version  : 0.1
  Bugs, Comments  : waveclaw@waveclaw.net
########################################################################
                          RELEVANT DOCUMENTS
                           (REFERENCES)

  Name                            Comment
  ------------------------------- -------------------------------------

########################################################################
                          REVISION HISTORY
 Date         Version(Build) SCM      Engineer Comment/Description
 DD-MMM-YYYY  Rel.Patch.Pnt  Reason
 -----------  -------------- -------- -------- -------------------------
 26-APR-2011  0.1/0.1(1)     WWW00661 jdpowell Copied from other scripts
########################################################################

"""
# turn on debugging
# import pdb; pdb.set_trace()

# parsing tools
import optparse
# Tkinter, the portable GUI
from tkinter import TclError
# Tix, the Tkinter extentions
import tkinter.tix as tix
#from Tkconstants import *

# pyaharef internals
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from view.gui import Gui

def main():
    """
    Display the GUI
    """
    rootWindow = tix.Tk() # not Tk, need the combo box widget
    rootWindow.wm_title('PyAharef Website Grapher')

    parser = optparse.OptionParser(version="0.0.74") # version option --version enabled
    parser.add_option("--verbose","-v", action="store_false", dest="verbose", help="be noisy", default=False)
    parser.add_option("--file","-f", action="store",type="string",dest="filename", help="what URL to probe")
    (options, arguments) = parser.parse_args() # ignoring arguments

    #if options.verbose:
    #   print(__doc__)

    if options.filename:
        file = options.filename
        graphgui = Gui(parent=rootWindow, url=file)
    else:
        graphgui = Gui(parent=rootWindow)
    rootWindow.mainloop()
    parser.destroy() # clean up cyclic references

if ( __name__ == '__main__' ):
    try:
       main()
    except TclError as tke:
        print(f'Error with Drawing the graphics {tke}')
    except Exception as e:
        print(f'An Error has occurred {e}')
        raise e
