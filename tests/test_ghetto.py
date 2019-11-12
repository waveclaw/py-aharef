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
        position = 1
        start    = [1, 1, 1]

class multiStyle:
        count    = 3
        position = 0
        start    = [0, 0, 0]

def similarTuple(left, right, max):
    """
      Compare the end return codes for tree.endpoint
    """
    for i in range(0, max):
        if left[i] > right[i]:
            if left[i] - right[i] > 0.5:
                return False
        else:
            if right[i] - left[i] > 0.5:
                return False
    return True

class GhettoDrawerTests(unittest.TestCase):
    """
     Ghetto Drawer is a (terrible) primitive physics simulation
    """
    def test_empty(self):
        """
         drawer should do nothing when there are no children
        """
        drawer = Ghetto(graph=None, tree=None, drawertype=emptyView)
        self.assertTrue(drawer.graph == None)
        self.assertTrue(drawer.tree == None)
        self.assertTrue(drawer.endpoint(None, emptyStyle, 0) == (0.0, 0.0, 0.0))

    def test_onelevel(self):
        """
         drawer should handle a tree with one node offset form (0,0)
        """
        drawer = Ghetto(graph=None, tree=None, drawertype=emptyView)
        self.assertTrue(drawer.graph == None)
        self.assertTrue(drawer.tree == None)
        self.assertTrue(similarTuple(drawer.endpoint(None, oneStyle, 0), (1.0, 1.0, 2.0), 3))


    def test_onelevel_at_depth(self):
        """
         drawer should handle a tree with one node at depth > 1 at (0,0)
        """
        drawer = Ghetto(graph=None, tree=None, drawertype=emptyView)
        self.assertTrue(drawer.graph == None)
        self.assertTrue(drawer.tree == None)
        self.assertTrue(similarTuple(drawer.endpoint(None, oneStyle, 2), (1.0, 1.0, 3.0), 3))

    def test_multilevel(self):

        """
         drawer should handle a tree with several nodes but nodepth
        """
        drawer = Ghetto(graph=None, tree=None, drawertype=emptyView)
        self.assertTrue(drawer.endpoint(None, multiStyle, 0) == (0.0, 0.0, 0.0))

    def test_multilevel_at_depth(self):

        """
         drawer should handle a tree with several nodes at depth > 1
        """
        drawer = Ghetto(graph=None, tree=None, drawertype=emptyView)
        self.assertTrue(drawer.endpoint(None, multiStyle, 2) == (0.0, 0.0, 0.0))

'''
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
'''
if __name__ == '__main__':
    unittest.main()
