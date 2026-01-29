from typing import Dict, Any, List
import pandas as pd

class HistoryFeatureExtractor:
    """
    Extracts features from the user_history list.
    """
    def __call__(self, example: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transforms a single example.
        Expected input: {'user_history': [...], 'item_bought': ...}
        """
        history = example.get('user_history', [])
        
        # Basic features
        num_events = len(history)
        view_events = [e for e in history if e['event_type'] == 'view']
        search_events = [e for e in history if e['event_type'] == 'search']
        
        # Update example with new features
        example['num_events'] = num_events
        example['num_views'] = len(view_events)
        example['num_searches'] = len(search_events)
        
        # Get last viewed item ID
        if view_events:
            last_view = view_events[-1]
            try:
                # event_info can be int (item_id) or string (search query)
                # For views, it should be item_id
                example['last_viewed_item'] = int(last_view.get('event_info'))
            except (ValueError, TypeError):
                 example['last_viewed_item'] = -1
        else:
            example['last_viewed_item'] = -1
            
        return example
