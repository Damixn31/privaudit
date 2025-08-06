import os
import json


def list_text_files(directory, extensions=None):
    if extensions is None:
        extensions = extensions or ['.txt', '.log', '.config', '.md', '.env', 'csv', '.json']

    file_list = []

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                file_list.append(os.path.join(root, file))
    return file_list

def load_rules(path="rules.json"):
    try:
        with open(path, "r") as f:
            rules = json.load(f)
            return rules
    except Exception as e:
        print(f"[!] Error cargando reglas: {e}")
        return []

