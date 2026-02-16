# Contributing to Protein Structure to Graph Converter

Thank you for considering contributing to this project! This document provides guidelines for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/protein-structure-graphs.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes thoroughly
6. Commit with clear messages: `git commit -m "Add feature: description"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install pytest black flake8 mypy
```

## Code Style

- Follow PEP 8 style guidelines
- Use type hints for function parameters and returns
- Include docstrings for all functions and classes
- Keep functions modular and focused on single responsibilities

### Example Function

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
    """
    # Implementation
    return True
```

## Testing

Before submitting a PR:

1. Test with various PDB files (monomer and complex structures)
2. Verify graph outputs are correct
3. Check that all summary files are generated
4. Ensure failed structures are properly logged

## Types of Contributions

### Bug Reports

When reporting bugs, include:
- Python version
- Operating system
- Installed package versions
- Minimal reproducible example
- Error messages and stack traces

### Feature Requests

When suggesting features:
- Explain the use case clearly
- Describe expected behavior
- Consider if it fits the tool's scope (structure → graph conversion only)

### Code Contributions

We welcome:
- Bug fixes
- Performance improvements
- Additional graph representations
- Documentation improvements
- New PDB parsing features
- Better error handling

We do NOT accept:
- Machine learning models or training code
- Protein language model embeddings
- Prediction/classification tasks
- Visualization tools (unless minimal and optional)

## Scientific Accuracy

For contributions affecting graph construction:
- Maintain scientific rigor in residue representation
- Document any changes to node/edge features clearly
- Ensure distance calculations are accurate
- Keep graph definitions mathematically sound

## Documentation

- Update README.md if adding features
- Add docstrings to new functions
- Update notebook cells if modifying pipeline
- Keep examples current and working

## Pull Request Process

1. **Title**: Clear, descriptive title (e.g., "Fix distance calculation bug" or "Add support for modified residues")
2. **Description**: Explain what changes were made and why
3. **Testing**: Describe how you tested the changes
4. **Breaking Changes**: Clearly note if changes break existing functionality

## Code Review

All PRs will be reviewed for:
- Code quality and style
- Scientific accuracy
- Documentation completeness
- Test coverage
- Backward compatibility

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Open an issue with the "question" label or start a discussion.

---

Thank you for helping make this tool better!
