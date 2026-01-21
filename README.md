# Criterio Ads

## Environment Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

### Prerequisites

- Install `uv`:
  ```bash
  # On macOS/Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh
  
  # On Windows
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

### Data Acquisition Process

To download the dataset, use the following command:

```bash
uv run kaggle datasets download marlesson/meli-data-challenge-2020
```

**Dataset Details:**
*   **Source:** [Kaggle - MercadoLibre Data Challenge 2020](https://www.kaggle.com/datasets/marlesson/meli-data-challenge-2020)
*   **License:** CC-BY-NC-SA-4.0
*   **Files:**
    *   `train_dataset.jl`: User history and bought item for training.
    *   `test_dataset.jl`: User history for testing.
    *   `item_data.jl`: Metadata for items.

The data should be unzipped into `data/raw/`.

### Architecture Overview

The project follows a modular structure:

*   `src/criterio_ads/`: Main package source code.
    *   `data/`: Data loading and processing modules.
    *   `models/`: Model definitions and training logic.
*   `data/`: Data directory (raw, processed).
*   `notebooks/`: Jupyter notebooks for exploration.

### Installation

To install the project dependencies:

```bash
uv sync
```

This will create a virtual environment (`.venv`) with all required packages.

### Running the Project

Run scripts using `uv run` to automatically use the project's environment:

```bash
uv run python src/train.py
```

### Common Commands

- **Add a package**: `uv add <package_name>`
- **Remove a package**: `uv remove <package_name>`
- **Update lockfile**: `uv lock`
