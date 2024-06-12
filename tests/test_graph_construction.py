import unittest
from collections import Counter
import networkx as nx
from gui import build_directed_graph  # 替换为实际的模块名


class TestBuildDirectedGraph(unittest.TestCase):

    def test_simple_text(self):
        text = "hello world"
        graph, word_count = build_directed_graph(text)

        expected_word_count = Counter({"hello": 1, "world": 1})
        self.assertEqual(word_count, expected_word_count)

        expected_edges = [("hello", "world")]
        self.assertEqual(list(graph.edges), expected_edges)

    def test_repeated_words(self):
        text = "hello hello world"
        graph, word_count = build_directed_graph(text)

        expected_word_count = Counter({"hello": 2, "world": 1})
        self.assertEqual(word_count, expected_word_count)

        expected_edges = [("hello", "hello"), ("hello", "world")]
        self.assertEqual(list(graph.edges), expected_edges)

    def test_complex_text(self):
        text = "a quick brown fox jumps over the lazy dog"
        graph, word_count = build_directed_graph(text)

        expected_word_count = Counter(text.split())
        self.assertEqual(word_count, expected_word_count)

        expected_edges = [(text.split()[i], text.split()[i + 1]) for i in range(len(text.split()) - 1)]
        self.assertEqual(list(graph.edges), expected_edges)


if __name__ == '__main__':
    unittest.main()
