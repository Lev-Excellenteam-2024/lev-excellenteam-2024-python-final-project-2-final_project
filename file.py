
import json
from typing import List, Dict

# Saves a list of slide summaries to a JSON file.
def save_to_json(filename: str, data: List[Dict[str, str]]):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
