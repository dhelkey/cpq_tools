import networkx as nx
import igraph as ig
import pandas as pd
import numpy as np

def dataframe_from_networkx(graph):
    """
    Create a DataFrame from a NetworkX graph.

    Each edge in the graph is represented by a row in the DataFrame.
    Edges with weight greater than 1 are replicated accordingly.

    Intended to construct sample datasets to test compute_network_metrics 

    Args:
    graph (nx.Graph): A NetworkX graph object.

    Returns:
    pd.DataFrame: DataFrame[['source', 'target']] representing edges of the graph.

    Example:
    >>> G = nx.Graph()
    >>> G.add_edge('A', 'B', weight=2)
    >>> G.add_edge('B', 'C', weight=1)
    >>> dataframe_from_networkx(G)
    """
    # Extract edges and their weights
    edges_with_weights = [(u, v, d.get('weight', 1)) for u, v, d in graph.edges(data=True)]

    # Create a DataFrame and replicate rows based on weight
    df = pd.DataFrame(edges_with_weights, columns=['source', 'target', 'weight'])
    df = df.loc[df.index.repeat(df['weight'])].reset_index(drop=True)
    #df.drop('weight', axis=1, inplace=True)
    return df

def print_graph_info(graph, graph_name = ''):
        """Print info of a networkX graph object
        """
        nodes = graph.nodes()
        edges = graph.edges(data=True)
        density = nx.density(graph)
        print(f"--- {graph_name} ---\n"
              f"Nodes ({len(nodes)}): {nodes}\n"
              f"Edges ({len(edges)}): {edges}\n"
              f"Density: {density:.4f}")

def print_network_nodes_edges(graph_networkx):
    """
    Prints the nodes, edges, and weights of a NetworkX graph.

    Args:
        graph_networkx (nx.Graph): A NetworkX graph object.

    Example:
        G = nx.Graph()
        G.add_edge(1, 2, weight=0.5)
        G.add_edge(2, 3, weight=1.5)
        print_network_nodes_edges(G)

    GPT-20230419
    """
    # Print nodes
    print("Nodes:", ", ".join(map(str, graph_networkx.nodes())))

    # Print edges with weights
    print("Edges:")
    for u, v, data in graph_networkx.edges(data=True):
        weight = data.get('weight', 1.0)  # Default weight is 1.0 if not specified
        print(f"({u}, {v}, weight={weight})")
# Example usage
# G = nx.Graph()
# G.add_edge(1, 2, weight=0.5)
# G.add_edge(2, 3, weight=1.5)
# print_network_nodes_edges(G)