import unittest
import networkx as nx
from gui import find_bridge_words, print_bridge_words  # 替换为实际的模块名

class TestBridgeWordsWhiteBox(unittest.TestCase):

    def setUp(self):
        # 创建一个示例有向图
        self.graph = nx.DiGraph()
        edges = [
            ("hello", "beautiful"),
            ("beautiful", "world"),
            ("hello", "amazing"),
            ("amazing", "world"),
            ("hello", "ugly"),
            ("ugly", "planet")
        ]
        self.graph.add_edges_from(edges)

    def test_find_bridge_words_word1_not_in_graph(self):
        result = find_bridge_words(self.graph, "not_in_graph", "world")
        self.assertIsNone(result)

    def test_find_bridge_words_word2_not_in_graph(self):
        result = find_bridge_words(self.graph, "hello", "not_in_graph")
        self.assertIsNone(result)

    def test_find_bridge_words_no_bridge_words(self):
        result = find_bridge_words(self.graph, "hello", "ugly")
        self.assertEqual(result, [])

    def test_find_bridge_words_one_bridge_word(self):
        result = find_bridge_words(self.graph, "hello", "planet")
        self.assertEqual(result, ["ugly"])

    def test_find_bridge_words_multiple_bridge_words(self):
        result = find_bridge_words(self.graph, "hello", "world")
        self.assertCountEqual(result, ["beautiful", "amazing"])

    def test_print_bridge_words_word1_not_in_graph(self):
        result = print_bridge_words(self.graph, "not_in_graph", "world")
        self.assertEqual(result, "No not_in_graph or world in the graph!")

    def test_print_bridge_words_word2_not_in_graph(self):
        result = print_bridge_words(self.graph, "hello", "not_in_graph")
        self.assertEqual(result, "No hello or not_in_graph in the graph!")

    def test_print_bridge_words_no_bridge_words(self):
        result = print_bridge_words(self.graph, "hello", "ugly")
        self.assertEqual(result, "No bridge words from hello to ugly!")

    def test_print_bridge_words_one_bridge_word(self):
        result = print_bridge_words(self.graph, "hello", "planet")
        self.assertEqual(result, "The bridge word from hello to planet is: ugly")

    def test_print_bridge_words_multiple_bridge_words(self):
        result = print_bridge_words(self.graph, "hello", "world")
        self.assertEqual(result, "The bridge words from hello to world are: beautiful, amazing")

if __name__ == '__main__':
    unittest.main()
