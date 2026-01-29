--- 
.PHONY: help setup data clean format lint test 


help:
	@echo "Available commands:"
	@echo "  make setup			- Create environment and install dependencies"
	@echo "  make data			- Download and process data"
	@echo "  make clean			- Remove generated files"
	@echo "  make format		- Format code with black"
	@echo "  make lint			- Run code quality checks"
	@echo "  make test			- Run tests"

setup:
	mamba env create -f environment.yml 
	@echo "Environment created! Activate with: mamba activate baseball-ml"

data:
	python scripts/download_data.py 

clean: 
	find . -type f -name "*.py[co]" -delete 
	find . -type d -name "__pycache__" -delete 
	rm -rf .pytest_cache 
	rm -rf htmlcov 
	rm -rf dist 
	rm -rf build 
	rm -rf *.egg-info 

format:
	black src/ scripts/ tests/
	isort src/ scripts/ tests/

lint:
	black --check src/ scripts/ tests/ 
	flake8 src/ scripts/ tests/ 
	mypy src/ 

test:
	pytest tests/
---
