# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-02-16

### Added
- Initial release of Protein Structure to Graph Converter
- Residue-level graph construction from PDB files
- Distance cutoff-based edge generation
- Support for monomer (single-chain) graph generation
- Support for complex (multi-chain) graph generation
- Configurable user parameters (distance cutoff, filtering options)
- Comprehensive node features (amino acid one-hot, residue index, chain ID, Cα coordinates)
- Edge features including distances and same-chain flags
- Batch processing of multiple PDB files
- Summary CSV generation for dataset statistics
- Failed structure logging with reasons
- Graph definition JSON export for reproducibility
- PyTorch Geometric output format
- Complete Jupyter notebook with modular functions
- Type hints throughout codebase
- Progress bars for batch processing
- Scientific transparency and documentation

### Features
- **Node Features**: 25-dimensional feature vector per residue
  - Amino acid one-hot encoding (20)
  - Residue index (1)
  - Chain ID encoded (1)
  - Cα xyz coordinates (3)
- **Edge Features**: 
  - Monomer mode: Distance (1)
  - Complex mode: Distance + same_chain_flag (2)
- **Filtering Options**:
  - Remove water residues
  - Remove heteroatoms
  - Minimum residue count per chain
- **Quality Control**:
  - PDB parsing validation
  - Missing Cα detection
  - Chain length validation
  - Error logging

### Documentation
- Comprehensive README with usage instructions
- Installation guide with requirements
- Scientific specification of graph definition
- Example code for loading and using graphs
- Contributing guidelines
- MIT License
- .gitignore for Python/Jupyter projects

## [Unreleased]

### Planned Features
- Support for additional graph formats (NetworkX, DGL)
- Optional residue-residue contact map generation
- Coordinate normalization options
- Secondary structure annotations
- Solvent accessible surface area features

---

For detailed information about each version, see the [Releases](https://github.com/yourusername/protein-structure-graphs/releases) page.
