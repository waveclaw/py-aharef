#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  Test the Ghetto physics engine
"""
from pyaharef.drawer.ghetto import Ghetto
import unittest

def emptyView(graph=None, tree=None, size=0, *kwargs):
    pass

class emptyStyle:
        count    = 0
        position = 0
        start    = [0, 0, 0]

class oneStyle:
        count    = 1
        position = 0
        start    = [0, 0, 0]

class multiStyle:
        count    = 3
        position = 0
        start    = [0, 0, 0]

class GhettoDrawerTests(unittest.TestCase):
    """
     Ghetto Drawer is a (terrible) primitive physics simulation
    """
    def test_empty(self):
        """
         drawer should do nothing
        """
        drawer = Ghetto(graph=None, tree=None, drawertype=emptyView)
        self.assertTrue(drawer.graph == None)
        self.assertTrue(drawer.tree == None)
        self.assertTrue(drawer.endpoint(None, emptyStyle, 0) == (0.0, 0.0, 0.0))

    def test_onelevel(self):
        """
         drawer should handle a tree with one node
        """
        drawer = Ghetto(graph=None, tree=None, drawertype=emptyView)
        self.assertTrue(drawer.graph == None)
        self.assertTrue(drawer.tree == None)
        self.assertTrue(drawer.endpoint(None, oneStyle, 0) == (0.0, 0.0, 0.0))


    def test_multilevel(self):
        """
         drawer should handle a tree with several nodes
        """
        drawer = Ghetto(graph=None, tree=None, drawertype=emptyView)
        self.assertTrue(drawer.endpoint(None, multiStyle, 0) == (0.0, 0.0, 0.0))

    def test_oneview(self):
        """
         drawer should handle a tree with one node and a sample view
        """
        drawer = Ghetto(graph=None, tree=None, drawertype=emptyView)
        self.assertTrue(drawer.graph == None)
        self.assertTrue(drawer.tree == None)

    def test_multiview(self):
        """
         drawer should handle a tree with several nodes and a sample view
        """
        pass

if __name__ == '__main__':
    unittest.main()
