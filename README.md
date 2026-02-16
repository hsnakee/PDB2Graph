# Protein Structure to Graph Converter

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-quality tool for converting PDB protein structures into residue-level graph representations for graph machine learning applications.

## Overview

This tool provides a clean, reproducible pipeline to transform protein structures (PDB format) into graph objects suitable for geometric deep learning. It supports both monomer (single-chain) and complex (multi-chain) graph generation with scientifically rigorous residue-level representations.

**Key Features:**
-  Residue-level graph construction using Cα atoms
-  Distance-based edge generation (user-configurable cutoff)
-  Support for monomer and multi-chain complex graphs
-  Rich node and edge features for ML applications
-  Batch processing of multiple PDB files
-  Comprehensive logging and validation
-  PyTorch Geometric output format
-  Production-ready, modular codebase

## Scientific Specification

### Graph Definition

**Nodes:** One node per residue with Cα atom present

**Node Features:**
- Amino acid one-hot encoding (20 standard amino acids)
- Residue index (sequential position)
- Chain ID (encoded)
- Cα xyz coordinates (3D spatial position)

**Edges:** 
- Undirected edges created when Cα-Cα distance ≤ cutoff threshold
- Edge features include exact Euclidean distance
- Bidirectional representation (both directions stored)

**Multi-chain graphs additionally include:**
- Same-chain flag (binary edge feature indicating intra- vs inter-chain edges)

## Installation

### Requirements
- Python 3.8+
- Jupyter Notebook or JupyterLab
- BioPython
- PyTorch
- PyTorch Geometric
- NumPy, pandas, tqdm

### Quick Setup

```bash
# Clone repository

cd protein-structure-graphs

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

## Usage

### 1. Prepare Your Data

Place your PDB files in a directory (e.g., `data/pdb_files/`).

### 2. Configure Parameters

Open `protein_graph_builder.ipynb` and edit the **User Configuration** cell:

```python
# ============================================================
# USER CONFIGURATION - EDIT THIS CELL ONLY
# ============================================================

# Input/Output Directories
INPUT_DIR = "data/pdb_files/"           # Folder containing PDB files
OUTPUT_DIR = "data/graphs/"             # Output directory for graphs

# Graph Construction Parameters
DISTANCE_CUTOFF_ANGSTROM = 8.0          # Cα-Cα distance cutoff (Å)

# Structure Filtering Options
REMOVE_WATER = True                      # Remove water residues
REMOVE_HETERO = True                     # Remove heteroatoms (ligands, ions)
MIN_RESIDUES = 10                        # Minimum residues per chain

# Output Format
SAVE_FORMAT = "pyg"                      # 'pyg' for PyTorch Geometric
```

### 3. Run the Notebook

Execute all cells sequentially. The notebook will:

- ✅ Parse PDB structures with validation
- ✅ Build residue-level graphs (monomer and complex modes)
- ✅ Save graph objects to disk
- ✅ Generate summary CSV files
- ✅ Log any processing errors

### Output Structure

```
data/graphs/
├── graphs_monomer/           # Single-chain graphs
│   ├── 1ABC_A.pt
│   ├── 1ABC_B.pt
│   └── ...
├── graphs_complex/           # Multi-chain complex graphs
│   ├── 1ABC_complex.pt
│   └── ...
├── dataset_summary_monomer.csv
├── dataset_summary_complex.csv
├── failed_structures.txt
└── graph_definition.json
```

## Graph Modes

### Monomer Mode
- **Purpose:** Analyze individual protein chains independently
- **Use case:** Single-domain proteins, chain-level classification
- **Edge behavior:** Only intra-chain edges (same chain)
- **Output:** One graph per chain

### Complex Mode
- **Purpose:** Analyze protein-protein interactions and assemblies
- **Use case:** Protein complexes, oligomers, interface prediction
- **Edge behavior:** Both intra-chain and inter-chain edges
- **Output:** One graph per structure (all chains combined)

## Examples

### Loading Generated Graphs

```python
import torch
from torch_geometric.data import Data

# Load monomer graph
graph = torch.load('data/graphs/graphs_monomer/1ABC_A.pt')

print(f"Nodes: {graph.num_nodes}")
print(f"Edges: {graph.num_edges}")
print(f"Node features shape: {graph.x.shape}")
print(f"Edge index shape: {graph.edge_index.shape}")
print(f"Edge attributes shape: {graph.edge_attr.shape}")

# Access node features
amino_acid_encoding = graph.x[:, :20]  # One-hot encoding
residue_indices = graph.x[:, 20]
chain_ids = graph.x[:, 21]
ca_coords = graph.x[:, 22:25]

# Access edge features
edge_distances = graph.edge_attr[:, 0]
```

### Batch Processing Statistics

After running the notebook, check the summary files:

```python
import pandas as pd

# Monomer statistics
df_monomer = pd.read_csv('data/graphs/dataset_summary_monomer.csv')
print(df_monomer.describe())

# Complex statistics
df_complex = pd.read_csv('data/graphs/dataset_summary_complex.csv')
print(df_complex.describe())
```

## Validation and Quality Control

The tool includes comprehensive validation:

- ✅ PDB parsing error handling
- ✅ Missing Cα atom detection
- ✅ Chain length validation
- ✅ Coordinate sanity checks
- ✅ Duplicate residue detection
- ✅ Failed structure logging

All skipped structures and reasons are logged to `failed_structures.txt`.

## Citation

If you use this tool in your research, please cite:

```bibtex
@software{protein_structure_graphs,
  title = {Protein Structure to Graph Converter},
  author = {Your Name},
  year = {2025},
  url = {https://github.com/yourusername/protein-structure-graphs}
}
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📖 [Documentation](https://github.com/yourusername/protein-structure-graphs/wiki)
- 🐛 [Issue Tracker](https://github.com/yourusername/protein-structure-graphs/issues)
- 💬 [Discussions](https://github.com/yourusername/protein-structure-graphs/discussions)

## Acknowledgments

- Built with [BioPython](https://biopython.org/) for PDB parsing
- Graph objects compatible with [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/)
- Inspired by research in geometric deep learning for protein science

---

**Note:** This tool is for structure-to-graph conversion only. It does not include protein language model embeddings, GNN training, or predictive models. For downstream ML tasks, use the generated graphs as input to your own models.
