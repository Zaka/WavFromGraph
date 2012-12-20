import unittest

import networkx as nx

import wav_from_graph.wav_from_graph as wfg

class TestWavFromGraph(unittest.TestCase):
    
    def setUp(self):
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from([(0, {'type':'concatenation'}), (1, {'type':'sample', 'value':1}), (2, {'type':'concatenation'}), (3, {'type':'sample', 'value':4}),
                                   (4, {'type':'sample', 'value':2}), (5, {'type':'sample', 'value':3})])
        self.graph.add_edges_from([(0,1),(0,2),(0,3),(2,4),(2,5)])
    
    def test_tree_root(self):
        g = self.graph.node[0]
        self.assertEqual(g, wfg.tree_root(self.graph))

    def test_flatten_graph(self):
        self.assertEqual([1,2,3,4],wfg.flatten_graph(self.graph, wfg.tree_root(self.graph)))
        