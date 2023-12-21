import unittest
import networkx as nx
import pandas as pd
import numpy as np

from cpq_tools.network_funs import compute_network_metrics, \
        print_network_nodes_edges, dataframe_from_networkx

class TestNetworkFunctions(unittest.TestCase):
    def test_network_metrics(self):
        #Generate test networks
        # (NOTE - Designed for DIRECTED networks)
        KARATE = nx.DiGraph(nx.karate_club_graph())
        KARATE_df = dataframe_from_networkx(KARATE)

        FLORENTINE = nx.DiGraph(nx.florentine_families_graph())
        FLORENTINE_df = dataframe_from_networkx(FLORENTINE)

        PETERSEN = nx.DiGraph(nx.petersen_graph())
        PETERSEN_df = dataframe_from_networkx(PETERSEN)

        G_directed = nx.DiGraph([(1, 2), (2, 3), (3, 4), (4, 2)])
        G_directed_df = dataframe_from_networkx(G_directed)

        G_directed = nx.DiGraph([(1, 2), (2, 3), (3, 4), (4, 2)])
        G_directed_df = dataframe_from_networkx(G_directed)

        G_disjoint = nx.DiGraph([(1, 2), (1, 3), (3, 2), (4, 1), (5, 6)])
        G_disjoint_df = dataframe_from_networkx(G_disjoint)

        G_ba = nx.barabasi_albert_graph(50, 3).to_directed()
        G_ba_df = dataframe_from_networkx(G_ba)

        networks = {
            'karate': (KARATE, KARATE_df),
            'directed': (G_directed, G_directed_df),
            'disjoint':(G_disjoint, G_disjoint_df),
            'barabasi_albert': (G_ba, G_ba_df),
            'florentine': (FLORENTINE, FLORENTINE_df),
            'petersen': (PETERSEN, PETERSEN_df) 
        }

        for network_name, (graph, df) in networks.items():
            with self.subTest(network=network_name):
                self.run_networkx_metrics(graph, df)

    def run_networkx_metrics(self, graph, df):
        #Output of function to be tested
        network_output = compute_network_metrics(df, 'source', 'target')

        df_metrics = network_output['df_metrics']

        graph_undirected = graph.to_undirected()

        #Compute network metrics manually
        num_nodes = graph.number_of_nodes()
        num_edges = graph.number_of_edges()
   
        density_unweighted = nx.density(graph)
        efficiency_global = nx.global_efficiency(graph_undirected)

         #Median local node efficiency
        local_efficiencies = []
        for node in graph_undirected.nodes():
            # Subgraph induced by the neighbors of the node
            neighbors = list(nx.neighbors(graph_undirected, node))
            if len(neighbors) < 2:
                # Local efficiency is zero if a node has less than two neighbors
                local_efficiencies.append(0)
                continue

            subgraph = graph_undirected.subgraph(neighbors)
            local_efficiency = nx.global_efficiency(subgraph)
            local_efficiencies.append(local_efficiency)

        # Calculate median of local efficiencies
        efficiency_median_local = np.median(local_efficiencies)
    

        katz_centralities = nx.katz_centrality_numpy(graph_undirected)
        in_degrees = dict(graph.in_degree())
        centrality_median = np.median(list(katz_centralities.values()))
        centrality_mean_receiving = np.mean([katz_centralities[node] for \
                        node, count in in_degrees.items() if count > 0])

        modularity_greedy = nx.algorithms.community.modularity(graph_undirected, 
            nx.algorithms.community.greedy_modularity_communities(graph_undirected))

        TOLERANCE = 1e-9
        self.assertEqual(num_nodes, df_metrics['n_nodes'])
        self.assertAlmostEqual(density_unweighted,
                                df_metrics['density_unweighted'] ,
                                delta = TOLERANCE)
        self.assertAlmostEqual(efficiency_global,
                                df_metrics['efficiency_global'],
                                delta = TOLERANCE)
        self.assertAlmostEqual(efficiency_median_local,
                                df_metrics['efficiency_median_local'],
                                delta = TOLERANCE)
        self.assertAlmostEqual(centrality_median,
                                df_metrics['centrality_median'],
                                delta = TOLERANCE)
        self.assertAlmostEqual(centrality_mean_receiving,
                                df_metrics['centrality_mean_receiving'],
                                delta = TOLERANCE)
        #Modularity (greedy) does not seem as percise
        self.assertAlmostEqual(modularity_greedy,
                                df_metrics['modularity_greedy'],
                                delta = 1e-2) 
        
        self.assertIsInstance(network_output['graph_networkx'],
                               nx.DiGraph)

if __name__ == '__main__':
    unittest.main()