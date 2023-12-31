import networkx as nx
import igraph as ig
import pandas as pd
import numpy as np

def compute_network_metrics(df_in, from_var='prevhsp', to_var='hospid', 
                        id_var=None, edge_cutoff=1, random_walk_steps = 5):
    """
    Construct network metrics from an individual-record level dataframe
    Parameters:
        df_in (DataFrame): Acute transfer DataFrame (One row per transfer).
        from_var (str): Source node.
        to_var (str): Destination node.
        id_var (str): Individual identifier.
        edge_cutoff (int): Minimum number of transfers to include an edge.
    Returns:
        dict: A dictionary containing the following key-value pairs:
            'df_metrics' (DataFrame): A DataFrame containing network metrics.
            'df_components' (DataFrame): A DataFrame of network components.
            'graph_networkx' (networkx.Graph): A NetworkX graph object representing the network.
            'graph_igraph' (igraph.Graph): An iGraph graph object representing the network.


    Code written by:
    Marinka Zitnik, Ph.D., Assistant Professor
    Email: marinka@hms.harvard.edu

    Compiled by:
    Daniel Helkey, MS
    Email: dhelkey@stanford.edu
    """
    df = df_in.copy()

    # #Treat nodes as strings 
    # df[from_var] = df[from_var].astype(str)
    # df[to_var] = df[to_var].astype(str)

    #Check for missing values
    variables_to_check = [from_var, to_var] + \
        ([id_var] if id_var is not None else [])
    for var in variables_to_check:
        if df[var].isnull().any():
            raise ValueError(f"Missing values in {var}.")
        #Treat all identifying variables as strings
        df[var] = df[var].astype(str)  

    #Identify number of nodes and individuals
    all_nodes = set(df[from_var]).union(set(df[to_var]))
        
    n_nodes = len(list(all_nodes))
    n_individuals = df[id_var].nunique() if id_var is not None else \
        len(df)

    #Compute observed edges
    edge_df = df.groupby([from_var, to_var]).size().reset_index(name='edge_weight')
    edge_df = edge_df[edge_df['edge_weight'] >= edge_cutoff]

    #Construct networkX representations 
    #G - directed networkX graph
    G = nx.DiGraph()
    G.add_nodes_from(all_nodes)
    G.add_weighted_edges_from(edge_df[[from_var, to_var, 'edge_weight']].values)
    #G_undirected - undirected networkX graph
    G_undirected = G.to_undirected()

    #Construct igraph representations 
    #g - Directed Igraph 
    g = ig.Graph(directed=True)
    g.add_vertices(sorted(set(edge_df[from_var]).union(edge_df[to_var])))
    edges = [(row[from_var], row[to_var]) for _, row in edge_df.iterrows()]
    weights = edge_df['edge_weight'].tolist()
    # Add edges with weights
    g.add_edges(edges)
    g.es['weight'] = weights
  
    #g_undirected - Undirected Igraph 
    #Note - not required for computing the current included network metrics
    g_undirected = g.as_undirected() 

    # Number of Connected Components
    num_connected_components = nx.number_connected_components(G_undirected)
    connected_components_list = list(nx.connected_components(G_undirected))

    # Nodes within Connected Components
    largest_connected_component_nodes = max(connected_components_list, key=len) if num_connected_components > 0 else set()
    max_node_percentage_by_component = len(largest_connected_component_nodes) / len(G_undirected) * 100  

    # Edge Weights within Connected Components 
    edge_weights = {(min(u, v), max(u, v)): data['weight'] for u, v, data in G_undirected.edges(data=True)}
    total_graph_weight = sum(edge_weights.values())

    def component_weight(component):
        """Calculate sum of component edge weights
        """
        return sum(edge_weights.get((min(u, v), max(u, v)), 0) for u, v in nx.edges(G_undirected.subgraph(component)))

    # Largest Weighted Component
    if num_connected_components > 1:
        largest_weighted_component = max(connected_components_list, key=component_weight)
        largest_component_weight = component_weight(largest_weighted_component)
    else:
        # Calculate the weight for the single component
        largest_component_weight = component_weight(connected_components_list[0]) if connected_components_list else 0

    # Calculate the percentage
    max_weight_percentage_by_component = largest_component_weight / total_graph_weight * 100

    #Sumary dataframe of connected comonentes
    components = list(nx.connected_components(G_undirected))
    df_components = pd.DataFrame([
        {
            'Component_Num': i + 1,  # Number components starting from 1
            'Component': component,
            'Node_Percentage': len(component) / len(G_undirected) * 100,
            'Weight_Percentage': component_weight(component) / total_graph_weight * 100
        }
        for i, component in enumerate(components)
    ])
    df_components.sort_values(by='Weight_Percentage', ascending=False, inplace=True)

    #Compute network metrics

    ## Efficiency
    #Global eficiency
    efficiency_global = nx.global_efficiency(G_undirected)
    
    #Median local node efficiency
    local_efficiencies = []
    for node in G_undirected.nodes():
        # Subgraph induced by the neighbors of the node
        neighbors = list(nx.neighbors(G_undirected, node))
        if len(neighbors) < 2:
            # Local efficiency is zero if a node has less than two neighbors
            local_efficiencies.append(0)
            continue

        subgraph = G_undirected.subgraph(neighbors)
        local_efficiency = nx.global_efficiency(subgraph)
        local_efficiencies.append(local_efficiency)
    efficiency_median_local = np.median(local_efficiencies)
    
    ## Density 
    #Unweighted density
    density_unweighted = nx.density(G)
    #Weighted density
    edge_weights = list(nx.get_edge_attributes(G, 'weight').values())
    density_weighted = np.sum(edge_weights) / (len(edge_weights) * np.max(edge_weights)) if \
                                                     edge_weights else 0

    ## Centrality
    katz_centralities = nx.katz_centrality_numpy(G_undirected)
    in_degrees = dict(G.in_degree())
    #Median node centrality 
    centrality_median = np.median(list(katz_centralities.values()))
    #Mean centrality of nodes with incoming transfers
    centrality_mean_receiving = np.mean([katz_centralities[node] for \
            node, count in in_degrees.items() if count > 0])
  
    ## Modularity
    #Greedy modularity
    modularity_greedy = nx.algorithms.community.modularity(G_undirected, 
        nx.algorithms.community.greedy_modularity_communities(G_undirected))
    #Random walk modularity
    giant_component = g.components(mode='weak').giant()
    random_walk = giant_component.community_walktrap(steps=5, weights=giant_component.es['weight']).as_clustering()
    modularity_randomwalk = giant_component.modularity(random_walk.membership)

    network_metrics = {
        'n_individuals': n_individuals,
        'n_nodes': len(all_nodes),
        'centrality_mean_receiving': centrality_mean_receiving,
        'centrality_median': centrality_median, #Centrality      
        'density_unweighted': density_unweighted,
        'density_weighted': density_weighted, #Density
        'efficiency_global': efficiency_global,
        'efficiency_median_local':efficiency_median_local, #Efficiency
        'modularity_randomwalk': modularity_randomwalk, #Modularity
        'modularity_greedy':modularity_greedy,
        'num_connected_components':num_connected_components,
        'max_node_percentage_by_component': max_node_percentage_by_component,
        'max_weight_percentage_by_component':max_weight_percentage_by_component 
    }
    
    return {
        'df_metrics':network_metrics,
        'df_components':df_components,
        'graph_networkx':G,
        'graph_network_igraph':g
    }

def dataframe_from_networkx(graph):
    """
    Create a DataFrame from a NetworkX graph.

    Each edge in the graph is represented by a row in the DataFrame.
    Edges with weight greater than 1 are replicated accordingly.

    Intended to construct sample datasets to test compute_network_metrics 

    Args:
    graph (nx.Graph): A NetworkX graph object.

    Returns:
    pd.DataFrame: DataFrame representing edges of the graph.

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