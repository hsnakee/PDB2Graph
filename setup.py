"""
Setup configuration for Protein Structure to Graph Converter.

This allows installation as a package (optional).
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="protein-structure-graphs",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Convert PDB protein structures to residue-level graphs for ML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/protein-structure-graphs",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "biopython>=1.79",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "torch>=2.0.0",
        "torch-geometric>=2.3.0",
        "tqdm>=4.62.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.910",
        ],
        "notebook": [
            "jupyter>=1.0.0",
            "notebook>=6.4.0",
            "ipykernel>=6.0.0",
        ],
    },
    keywords="protein structure graph neural network bioinformatics pytorch geometric",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/protein-structure-graphs/issues",
        "Source": "https://github.com/yourusername/protein-structure-graphs",
        "Documentation": "https://github.com/yourusername/protein-structure-graphs/wiki",
    },
)
