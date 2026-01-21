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
