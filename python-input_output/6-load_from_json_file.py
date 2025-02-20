import sys
import os
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if Path(filename).exists():
    items = load_from_json_file(filename)
else:
    items = []

# Add command-line arguments (excluding script name) to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)

