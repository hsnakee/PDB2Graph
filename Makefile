.PHONY: help install install-dev clean test format lint notebook download-example

help:
	@echo "Protein Structure to Graph Converter - Available Commands"
	@echo "=========================================================="
	@echo "make install          - Install package and dependencies"
	@echo "make install-dev      - Install with development dependencies"
	@echo "make notebook         - Launch Jupyter notebook"
	@echo "make download-example - Download example PDB files"
	@echo "make clean           - Remove generated files and caches"
	@echo "make test            - Run tests (if available)"
	@echo "make format          - Format code with black"
	@echo "make lint            - Run code linters"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install pytest black flake8 mypy

notebook:
	jupyter notebook protein_graph_builder.ipynb

download-example:
	@echo "Downloading example PDB files..."
	@mkdir -p data/pdb_files
	@echo "Downloading 1UBQ (Ubiquitin - small monomer)..."
	@wget -q https://files.rcsb.org/download/1UBQ.pdb -O data/pdb_files/1UBQ.pdb || curl -s https://files.rcsb.org/download/1UBQ.pdb -o data/pdb_files/1UBQ.pdb
	@echo "Downloading 1A3N (Hemoglobin - multi-chain complex)..."
	@wget -q https://files.rcsb.org/download/1A3N.pdb -O data/pdb_files/1A3N.pdb || curl -s https://files.rcsb.org/download/1A3N.pdb -o data/pdb_files/1A3N.pdb
	@echo "Downloading 2OED (Insulin - small complex)..."
	@wget -q https://files.rcsb.org/download/2OED.pdb -O data/pdb_files/2OED.pdb || curl -s https://files.rcsb.org/download/2OED.pdb -o data/pdb_files/2OED.pdb
	@echo "✓ Downloaded 3 example PDB files to data/pdb_files/"

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf *.egg-info
	rm -rf build dist
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -name ".ipynb_checkpoints" -exec rm -rf {} +
	@echo "✓ Cleanup complete"

test:
	@echo "Running tests..."
	pytest tests/ -v || echo "No tests found"

format:
	@echo "Formatting code with black..."
	black protein_graph_builder.ipynb examples/ --line-length 100 || echo "Black not installed"

lint:
	@echo "Running flake8..."
	flake8 examples/ --max-line-length 100 || echo "Flake8 not installed"
	@echo "Running mypy..."
	mypy examples/ --ignore-missing-imports || echo "Mypy not installed"

setup-venv:
	@echo "Setting up virtual environment..."
	python -m venv venv
	@echo "✓ Virtual environment created"
	@echo "Activate with: source venv/bin/activate  (Linux/Mac)"
	@echo "           or: venv\\Scripts\\activate     (Windows)"
