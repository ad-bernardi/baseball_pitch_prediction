---
# Setup Guide 

## Prerequisites

- Python 3.11+
- Mamba/Conda or pip 
- Git 

## Installation Steps 

### 1. Clone Repository 
```bash
git clone https://github.com/ad-bernardi/baseball_pitch_prediction
cd baseball_pitch_prediction
```

### 2. Create Environment 
```bash 
# Using Mamba (recommended)
mamba env create -f environment.yml 
mamba activate baseball_ml 

# or using conda 
conda env create -f environment.yml 
conda activate baseball_ml

# or using pip 
python -m venv venv 
source venv/bin/activate 
pip install -r requirements-dev.txt
```

### 3. Install project 
```bash 
pip install -e
```

### 4. Verify installation 
```bash 
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "from src.utils import config; print('Config loaded!')"
```

### 5. Download Data 
```bash 
python scripts/download_data.py 
```

## Troubleshooting 

### Environment Creation Fails 
```bash 
# Clean conda cache 
mamba clean --all 

# try again 
mamba env create -f environment.yml 
```

### Import Errors 
```bash
# Reinstall project 
pip install -e 
```

## Next Steps
See the main README.md for usage instructions beyond this. Have fun!
---











---
