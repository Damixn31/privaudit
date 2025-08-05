import os

def list_text_files(start_path, extensions=None):
    extensions = extensions or ['.txt', '.log', '.config', '.md', '.env']
    all_files = []

    for root, _, files in os.walk(start_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                all_files.append(os.path.join(root, file))
    return all_files
