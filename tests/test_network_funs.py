import unittest
import networkx as nx
import pandas as pd

from cpq_tools.network_funs import compute_network_metrics

class TestNetworkFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Initialize sample datasets to test network functionality

        col_names = ['from_col', 'to_col']

        # Initialize Karate Club graph
        cls.KARATE = nx.karate_club_graph()
        cls.KARATE_df = pd.DataFrame(list(cls.KARATE.edges()), columns=col_names)

        # Initialize Florentine Families graph
        cls.FLORENTINE = nx.florentine_families_graph()
        cls.FLORENTINE_df = pd.DataFrame(list(cls.FLORENTINE.edges()), columns=col_names)

        # Initialize Petersen graph
        cls.PETERSEN = nx.petersen_graph()
        cls.PETERSEN_df = pd.DataFrame(list(cls.PETERSEN.edges()), columns=col_names)

    def test_network_metrics_karate(self):
        self.test_networkx_metrics(self.KARATE, self.KARATE_df)

    def test_network_metrics_florentine(self):
        self.test_networkx_metrics(self.FLORENTINE, self.FLORENTINE_df)

    def test_network_metrics_petersen(self):
        self.test_networkx_metrics(self.PETERSEN, self.PETERSEN_df)

    def test_networkx_metrics(self, graph, df):
        #Output of function to be tested
        network_metrics = compute_network_metrics(df, 'from_col', 'to_col')
        
        print(df.head(2))
        print('')

        num_nodes = graph.number_of_nodes()
        num_edges = graph.number_of_edges()
        density = nx.density(graph)
        global_efficiency = nx.global_efficiency(graph)

        print(f"Network: {num_nodes} nodes, {num_edges} edges, Density: {density}, Global Efficiency: {global_efficiency}")
        self.assertIsNotNone(num_nodes)
        self.assertIsNotNone(num_edges)
        self.assertGreaterEqual(density, 0)
        self.assertGreaterEqual(global_efficiency, 0)



if __name__ == '__main__':
    unittest.main()