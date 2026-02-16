# Quick Start Guide

Get up and running with the Protein Structure to Graph Converter in 5 minutes.

## Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- At least one PDB file

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/protein-structure-graphs.git
cd protein-structure-graphs
```

### 2. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Example PDB Files

```bash
# Create data directory if it doesn't exist
mkdir -p data/pdb_files

# Download example structure (Hemoglobin - 1A3N)
wget https://files.rcsb.org/download/1A3N.pdb -P data/pdb_files/

# Or using curl
curl https://files.rcsb.org/download/1A3N.pdb -o data/pdb_files/1A3N.pdb
```

**More example structures:**
- `1A3N` - Hemoglobin (multi-chain)
- `1UBQ` - Ubiquitin (small monomer)
- `2OED` - Insulin (small complex)
- `6LU7` - SARS-CoV-2 Main Protease

## Running the Tool

### 5. Launch Jupyter

```bash
jupyter notebook
```

This will open Jupyter in your browser.

### 6. Open the Notebook

Navigate to and open: `protein_graph_builder.ipynb`

### 7. Configure Parameters

Find the **User Configuration** cell (Section 3) and edit:

```python
# ============================================================
# USER CONFIGURATION - EDIT THIS CELL ONLY
# ============================================================

INPUT_DIR = "data/pdb_files/"           # Your PDB files location
OUTPUT_DIR = "data/graphs/"             # Where to save graphs
DISTANCE_CUTOFF_ANGSTROM = 8.0          # Distance threshold
```

### 8. Run All Cells

In Jupyter menu: **Cell → Run All**

Or use keyboard shortcut: `Shift + Enter` through each cell

## Output

After running, you'll find:

```
data/graphs/
├── graphs_monomer/
│   ├── 1A3N_A.pt
│   ├── 1A3N_B.pt
│   └── ...
├── graphs_complex/
│   └── 1A3N_complex.pt
├── dataset_summary_monomer.csv
├── dataset_summary_complex.csv
└── graph_definition.json
```

## Verify Results

### Check Summary Files

```bash
# View monomer statistics
cat data/graphs/dataset_summary_monomer.csv

# View complex statistics
cat data/graphs/dataset_summary_complex.csv
```

### Load a Graph in Python

```python
import torch

# Load a monomer graph
graph = torch.load('data/graphs/graphs_monomer/1A3N_A.pt')

print(f"Nodes: {graph.num_nodes}")
print(f"Edges: {graph.num_edges}")
print(f"Node features: {graph.x.shape}")
print(f"Edge features: {graph.edge_attr.shape}")
```

## Next Steps

### Option 1: Process Your Own PDB Files

1. Place your `.pdb` files in `data/pdb_files/`
2. Re-run the notebook

### Option 2: Use Generated Graphs

```python
# Example: Create a dataset
from examples.load_graphs import ProteinGraphDataset

dataset = ProteinGraphDataset(root='data/graphs/graphs_monomer')
print(f"Loaded {len(dataset)} graphs")

# Use with PyTorch Geometric DataLoader
from torch_geometric.data import DataLoader

loader = DataLoader(dataset, batch_size=32, shuffle=True)
for batch in loader:
    # Your training code here
    pass
```

### Option 3: Experiment with Parameters

Try different cutoff values to see how graph connectivity changes:

```python
# Sparse graphs (fewer edges)
DISTANCE_CUTOFF_ANGSTROM = 5.0

# Dense graphs (more edges)
DISTANCE_CUTOFF_ANGSTROM = 10.0
```

## Troubleshooting

### Issue: "No module named 'Bio'"

**Solution:** Install BioPython
```bash
pip install biopython
```

### Issue: "No PDB files found"

**Solution:** Check your INPUT_DIR path
```python
import os
print(os.path.exists("data/pdb_files/"))
print(os.listdir("data/pdb_files/"))
```

### Issue: "All structures failed"

**Solution:** Check `failed_structures.txt` for reasons
```bash
cat data/graphs/failed_structures.txt
```

Common reasons:
- PDB file corrupted
- No valid chains (all heteroatoms/water)
- Too few residues

### Issue: Out of memory

**Solution:** Process fewer files at once or increase system memory

## Common Workflows

### Workflow 1: Research Dataset Preparation

```bash
# 1. Download structures from RCSB
wget https://files.rcsb.org/download/XXXX.pdb -P data/pdb_files/

# 2. Run notebook
jupyter notebook protein_graph_builder.ipynb

# 3. Analyze results
python examples/load_graphs.py
```

### Workflow 2: AlphaFold Structures

```bash
# Download AlphaFold predictions
# Place in data/pdb_files/

# Run with same parameters
# AlphaFold structures are typically monomers
```

### Workflow 3: Protein-Protein Complexes

```python
# Use complex mode for interface analysis
OUTPUT_DIR = "data/graphs/"

# Generated graphs will include inter-chain edges
# Check edge_attr[:, 1] for same_chain_flag
```

## Getting Help

- **Documentation**: See [README.md](README.md)
- **Issues**: Open an issue on GitHub
- **Examples**: Check `examples/` directory
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## Performance Tips

1. **Large datasets**: Process in batches
2. **GPU**: Not needed (CPU is sufficient)
3. **Memory**: ~100MB per 1000 residues
4. **Speed**: ~1-2 seconds per structure

---

**You're ready!** Start converting protein structures to graphs for your ML projects.
