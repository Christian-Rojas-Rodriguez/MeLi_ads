import pandas as pd
import os
from pathlib import Path
from typing import Optional, Dict, Any, List

class MeliChallengeDataset:
    """
    Dataset handler for the Mercado Libre Data Challenge 2020.
    """
    def __init__(self, 
                 data_dir: str = "data/raw", 
                 train_filename: str = "train_dataset.jl",
                 test_filename: str = "test_dataset.jl",
                 item_filename: str = "item_data.jl",
                 transform: Optional[Any] = None):
        
        self.transform = transform
        
        self.data_dir = Path(data_dir)
        self.train_path = self.data_dir / train_filename
        self.test_path = self.data_dir / test_filename
        self.item_path = self.data_dir / item_filename
        
        self.train_data: Optional[pd.DataFrame] = None
        self.test_data: Optional[pd.DataFrame] = None
        self.item_data: Optional[pd.DataFrame] = None

    def load_train(self, nrows: Optional[int] = None) -> pd.DataFrame:
        """Loads the training dataset."""
        if not self.train_path.exists():
            raise FileNotFoundError(f"Train file not found at {self.train_path}")
            
        print(f"Loading train data from {self.train_path}...")
        self.train_data = pd.read_json(self.train_path, lines=True, nrows=nrows)
        return self.train_data

    def load_test(self, nrows: Optional[int] = None) -> pd.DataFrame:
        """Loads the test dataset."""
        if not self.test_path.exists():
            raise FileNotFoundError(f"Test file not found at {self.test_path}")
            
        print(f"Loading test data from {self.test_path}...")
        self.test_data = pd.read_json(self.test_path, lines=True, nrows=nrows)
        return self.test_data

    def load_items(self, nrows: Optional[int] = None) -> pd.DataFrame:
        """Loads item metadata."""
        if not self.item_path.exists():
            raise FileNotFoundError(f"Item file not found at {self.item_path}")
            
        print(f"Loading item data from {self.item_path}...")
        self.item_data = pd.read_json(self.item_path, lines=True, nrows=nrows)
        return self.item_data

    def get_example(self, index: int, dataset: str = 'train') -> Dict[str, Any]:
        """Returns a single example from the loaded dataset."""
        if dataset == 'train':
            if self.train_data is None:
                raise ValueError("Train data not loaded. Call load_train() first.")
            data = self.train_data.iloc[index].to_dict()
        elif dataset == 'test':
            if self.test_data is None:
                raise ValueError("Test data not loaded. Call load_test() first.")
            data = self.test_data.iloc[index].to_dict()
        else:
            raise ValueError("dataset must be 'train' or 'test'")
            
        if self.transform:
            data = self.transform(data)
            
        return data

if __name__ == "__main__":
    # Example usage
    # Adjust path if running from a different directory, or ensure cwd is project root
    project_root = Path(__file__).resolve().parents[3]
    data_dir = project_root / "data" / "raw"
    
    dataset = MeliChallengeDataset(data_dir=str(data_dir))
    
    try:
        # Load a small sample to verify
        print("Loading sample train data...")
        df_train = dataset.load_train(nrows=5)
        print("Train data shape:", df_train.shape)
        print("Columns:", df_train.columns)
        print("First row:", df_train.iloc[0])
        
        print("\nLoading sample item data...")
        df_items = dataset.load_items(nrows=5)
        print("Item data shape:", df_items.shape)
        print("Columns:", df_items.columns)
        
    except FileNotFoundError as e:
        print(e)
