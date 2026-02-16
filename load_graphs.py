#!/usr/bin/env python3
"""
Example script demonstrating how to load and use generated protein graphs.

This script shows:
1. Loading individual graph files
2. Accessing node and edge features
3. Creating PyTorch Geometric datasets
4. Basic graph statistics and visualization
"""

import torch
from torch_geometric.data import Data, Dataset
from pathlib import Path
import numpy as np
import pandas as pd
from typing import List


def load_single_graph(graph_path: str) -> Data:
    """
    Load a single graph from disk.
    
    Args:
        graph_path: Path to .pt graph file
        
    Returns:
        PyTorch Geometric Data object
    """
    graph = torch.load(graph_path)
    return graph


def inspect_graph(graph: Data) -> None:
    """
    Print detailed information about a graph.
    
    Args:
        graph: PyTorch Geometric Data object
    """
    print(f"Graph Statistics:")
    print(f"  Nodes: {graph.num_nodes}")
    print(f"  Edges: {graph.num_edges}")
    print(f"  Node features shape: {graph.x.shape}")
    print(f"  Edge index shape: {graph.edge_index.shape}")
    print(f"  Edge attributes shape: {graph.edge_attr.shape}")
    
    # Extract and analyze features
    amino_acid_onehot = graph.x[:, :20]
    residue_indices = graph.x[:, 20]
    chain_ids = graph.x[:, 21]
    ca_coords = graph.x[:, 22:25]
    
    print(f"\nNode Feature Details:")
    print(f"  Amino acid encoding: [:, 0:20] (one-hot)")
    print(f"  Residue indices range: {residue_indices.min():.0f} - {residue_indices.max():.0f}")
    print(f"  Unique chains: {len(torch.unique(chain_ids))}")
    print(f"  Coordinate bounds:")
    print(f"    X: [{ca_coords[:, 0].min():.2f}, {ca_coords[:, 0].max():.2f}]")
    print(f"    Y: [{ca_coords[:, 1].min():.2f}, {ca_coords[:, 1].max():.2f}]")
    print(f"    Z: [{ca_coords[:, 2].min():.2f}, {ca_coords[:, 2].max():.2f}]")
    
    # Edge analysis
    edge_distances = graph.edge_attr[:, 0]
    print(f"\nEdge Statistics:")
    print(f"  Distance range: {edge_distances.min():.2f} - {edge_distances.max():.2f} Å")
    print(f"  Mean distance: {edge_distances.mean():.2f} Å")
    print(f"  Median distance: {edge_distances.median():.2f} Å")
    
    # Check if complex graph (has same_chain_flag)
    if graph.edge_attr.shape[1] > 1:
        same_chain_flags = graph.edge_attr[:, 1]
        num_inter_chain = (same_chain_flags == 0).sum().item()
        print(f"  Inter-chain edges: {num_inter_chain}")
        print(f"  Intra-chain edges: {graph.num_edges - num_inter_chain}")


class ProteinGraphDataset(Dataset):
    """
    PyTorch Geometric Dataset for protein graphs.
    
    Example usage:
        dataset = ProteinGraphDataset(root='data/graphs/graphs_monomer')
        loader = DataLoader(dataset, batch_size=32, shuffle=True)
    """
    
    def __init__(self, root: str, transform=None, pre_transform=None):
        """
        Args:
            root: Root directory containing .pt graph files
            transform: Optional transform to apply to each graph
            pre_transform: Optional pre-transform to apply once
        """
        self.root = Path(root)
        self.graph_files = sorted(list(self.root.glob("*.pt")))
        super().__init__(root, transform, pre_transform)
    
    def len(self) -> int:
        """Return the number of graphs in the dataset."""
        return len(self.graph_files)
    
    def get(self, idx: int) -> Data:
        """
        Load and return a single graph.
        
        Args:
            idx: Index of graph to load
            
        Returns:
            PyTorch Geometric Data object
        """
        graph_path = self.graph_files[idx]
        graph = torch.load(graph_path)
        return graph


def compute_graph_statistics(graphs_dir: str) -> pd.DataFrame:
    """
    Compute statistics for all graphs in a directory.
    
    Args:
        graphs_dir: Directory containing .pt graph files
        
    Returns:
        DataFrame with statistics for each graph
    """
    graph_files = list(Path(graphs_dir).glob("*.pt"))
    
    stats = []
    for graph_file in graph_files:
        graph = torch.load(graph_file)
        
        edge_distances = graph.edge_attr[:, 0]
        
        stats.append({
            'filename': graph_file.name,
            'num_nodes': graph.num_nodes,
            'num_edges': graph.num_edges,
            'avg_degree': graph.num_edges / graph.num_nodes if graph.num_nodes > 0 else 0,
            'min_distance': edge_distances.min().item(),
            'max_distance': edge_distances.max().item(),
            'mean_distance': edge_distances.mean().item(),
        })
    
    return pd.DataFrame(stats)


def extract_coordinates(graph: Data) -> np.ndarray:
    """
    Extract Cα coordinates from a graph.
    
    Args:
        graph: PyTorch Geometric Data object
        
    Returns:
        NumPy array of shape (num_nodes, 3) with xyz coordinates
    """
    ca_coords = graph.x[:, 22:25].numpy()
    return ca_coords


def get_amino_acid_sequence(graph: Data) -> List[str]:
    """
    Extract amino acid sequence from graph.
    
    Args:
        graph: PyTorch Geometric Data object
        
    Returns:
        List of amino acid three-letter codes
    """
    # Standard amino acids in order
    amino_acids = [
        'ALA', 'CYS', 'ASP', 'GLU', 'PHE',
        'GLY', 'HIS', 'ILE', 'LYS', 'LEU',
        'MET', 'ASN', 'PRO', 'GLN', 'ARG',
        'SER', 'THR', 'VAL', 'TRP', 'TYR'
    ]
    
    # Get one-hot encoded amino acids
    aa_onehot = graph.x[:, :20]
    aa_indices = aa_onehot.argmax(dim=1).numpy()
    
    sequence = [amino_acids[idx] for idx in aa_indices]
    return sequence


# Example usage
if __name__ == "__main__":
    print("Protein Graph Loading Examples\n")
    print("=" * 60)
    
    # Example 1: Load and inspect a single graph
    print("\n1. Loading a single graph:")
    print("-" * 60)
    
    # Update this path to point to an actual graph file
    example_graph = "data/graphs/graphs_monomer/example_A.pt"
    
    if Path(example_graph).exists():
        graph = load_single_graph(example_graph)
        inspect_graph(graph)
    else:
        print(f"Graph file not found: {example_graph}")
        print("Please run the notebook first to generate graphs.")
    
    # Example 2: Create a dataset
    print("\n\n2. Creating a dataset:")
    print("-" * 60)
    
    graphs_dir = "data/graphs/graphs_monomer"
    if Path(graphs_dir).exists() and len(list(Path(graphs_dir).glob("*.pt"))) > 0:
        dataset = ProteinGraphDataset(root=graphs_dir)
        print(f"Dataset created with {len(dataset)} graphs")
        
        # Access first graph
        if len(dataset) > 0:
            first_graph = dataset[0]
            print(f"First graph: {first_graph.num_nodes} nodes, {first_graph.num_edges} edges")
    else:
        print(f"No graphs found in {graphs_dir}")
    
    # Example 3: Compute statistics
    print("\n\n3. Computing dataset statistics:")
    print("-" * 60)
    
    if Path(graphs_dir).exists() and len(list(Path(graphs_dir).glob("*.pt"))) > 0:
        stats_df = compute_graph_statistics(graphs_dir)
        print(f"\nDataset Statistics:")
        print(stats_df.describe())
        
        # Save to CSV
        stats_df.to_csv('graph_statistics.csv', index=False)
        print("\nStatistics saved to: graph_statistics.csv")
    
    print("\n" + "=" * 60)
    print("Examples complete!")
