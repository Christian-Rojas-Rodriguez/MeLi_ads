import os
import subprocess
from pathlib import Path
import sys

def download_data():
    """
    Downloads the Meli Data Challenge 2020 dataset using Kaggle API.
    """
    # Define paths relative to the project root
    # assuming this script is in src/criterio_ads/data/
    project_root = Path(__file__).resolve().parents[3]
    data_raw_dir = project_root / "data" / "raw"
    
    # Check if data exists
    required_files = ["train_dataset.jl", "test_dataset.jl", "item_data.jl"]
    missing_files = [f for f in required_files if not (data_raw_dir / f).exists()]
    
    if not missing_files:
        print(f"Data already exists in {data_raw_dir}")
        return

    print(f"Missing files: {missing_files}")
    print("Downloading dataset from Kaggle...")
    
    # Ensure directory exists
    data_raw_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Check if uv is available
        import shutil
        has_uv = shutil.which("uv") is not None
        
        cmd = ["uv", "run", "kaggle", "datasets", "download", "marlesson/meli-data-challenge-2020"]
        if not has_uv:
            print("fast-tracking: uv not found, trying direct kaggle execution")
            cmd = ["kaggle", "datasets", "download", "marlesson/meli-data-challenge-2020"]

        # Run the download command
        subprocess.run(
            cmd,
            check=True,
            cwd=project_root # Run from project root
        )
        
        # Unzip
        zip_path = project_root / "meli-data-challenge-2020.zip"
        if zip_path.exists():
            print(f"Unzipping {zip_path} to {data_raw_dir}...")
            subprocess.run(
                ["unzip", "-o", str(zip_path), "-d", str(data_raw_dir)],
                check=True
            )
            # Optional: remove zip file? Keeping it for now as per "download" intent.
        else:
            print("Zip file not found after download command.")

    except subprocess.CalledProcessError as e:
        print(f"Error during download or unzip: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_data()
