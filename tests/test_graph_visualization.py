import unittest
import networkx as nx
from gui import show_directed_graph  # 替换为实际的模块名


class TestShowDirectedGraph(unittest.TestCase):

    def test_show_simple_graph(self):
        graph = nx.DiGraph()
        graph.add_edge("hello", "world", weight=1)

        try:
            show_directed_graph(graph)
        except Exception as e:
            self.fail(f"show_directed_graph raised an exception: {e}")

    def test_show_highlighted_path(self):
        graph = nx.DiGraph()
        graph.add_edge("start", "middle", weight=1)
        graph.add_edge("middle", "end", weight=1)

        try:
            show_directed_graph(graph, highlighted_path=["start", "middle", "end"])
        except Exception as e:
            self.fail(f"show_directed_graph raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
