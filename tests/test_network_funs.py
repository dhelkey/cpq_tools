import unittest
import networkx as nx
import pandas as pd
import numpy as np

from cpq_tools.network_funs import compute_network_metrics, \
        print_network_nodes_edges, dataframe_from_networkx

class TestNetworkFunctions(unittest.TestCase):
    def test_network_metrics(self):
        #Generate test networks
        KARATE = nx.DiGraph(nx.karate_club_graph())

        FLORENTINE = nx.DiGraph(nx.florentine_families_graph())

        PETERSEN = nx.DiGraph(nx.petersen_graph())

        G_empty = nx.DiGraph()

        G_tiny = nx.DiGraph([(1, 2)])

        G_directed = nx.DiGraph([(1, 2), (2, 3), (3, 4), (4, 2)])

        G_directed = nx.DiGraph([(1, 2), (2, 3), (3, 4), (4, 2)])

        G_disjoint = nx.DiGraph([(1, 2), (1, 3), (3, 2), (4, 1), (5, 6)])

        G_loops = nx.DiGraph([(1, 2), (3, 3), (3, 2), (4, 1), (5, 6), (6,6)])
 
        G_ba = nx.barabasi_albert_graph(50, 3).to_directed()
      
        networks = {
            'karate': KARATE,
            'directed': G_directed,
            'disjoint': G_disjoint,
            'barabasi_albert': G_ba,
            'florentine': FLORENTINE,
            'petersen': PETERSEN ,
            'tiny':G_tiny,
            'loops':G_loops
        }

        # Function to add missing weights (assume this exists)
        def ensure_edge_weights(graph, default_weight=1.0):
            for u, v, data in graph.edges(data=True):
                if 'weight' not in data:
                    data['weight'] = default_weight

        # Update each network with weights (if not specified)
        for network_name, graph in networks.items():
            ensure_edge_weights(graph)

        #Create network_data dictionary of - (graph, df) tuples
        network_data = {}
        for network_name, graph in networks.items():
            network_data[network_name] = (graph, dataframe_from_networkx(graph))

        for network_name, (graph, df) in network_data.items():
            with self.subTest(network=network_name):
                self.run_networkx_metrics(graph, df)

    def run_networkx_metrics(self, graph, df):
        #Output of function to be tested
        test = graph.edges(data=True)
        edge_weights = list(nx.get_edge_attributes(graph,
                                                 'weight').values())

        graph_undirected = graph.to_undirected()

        #Compute network metrics manually
        num_nodes = graph.number_of_nodes()
        num_edges = graph.number_of_edges()
        n_transfers = df.shape[0]
        n_self_loops = df[df['source'] == df['target']].shape[0]
    
        #Density
        density_unweighted = nx.density(graph)
        
        density_weighted = np.sum(edge_weights) /  \
            (len(edge_weights) * np.max(edge_weights)) if \
                                    edge_weights else 0

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

        #Test network code
        network_output = compute_network_metrics(df, 'source', 'target')
        df_metrics = network_output['df_metrics']

        n_transfers = df.shape[0]

        TOLERANCE = 1e-9
        self.assertEqual(num_nodes, df_metrics['n_nodes'])
        self.assertEqual(n_transfers, df_metrics['n_transfers'])
        self.assertEqual(n_self_loops, df_metrics['n_self_loops'])
        self.assertAlmostEqual(density_unweighted,
                                df_metrics['density_unweighted'] ,
                                delta = TOLERANCE)
        self.assertAlmostEqual(density_weighted,
                                df_metrics['density_weighted'] ,
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
        #Modularity (greedy) does not seem as precise
        self.assertAlmostEqual(modularity_greedy,
                                df_metrics['modularity_greedy'],
                                delta = 1e-4) 
        
        self.assertIsInstance(network_output['graph_networkx'],
                               nx.DiGraph)

if __name__ == '__main__':
    unittest.main()