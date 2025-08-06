import re
from .regex_patterns import PATTERNS

def scan_file(filepath, rules):
    results = []

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f, 1):
                for rule in rules:
                    matches = re.findall(rule["pattern"], line)
                    for match in matches:
                        results.append({
                            "type": rule["type"],
                            "match": match,
                            "file": filepath,
                            "line": i
                        })
    except Exception as e:
        print(f"[!] Error leyendo {filepath}: {e}")
    
    return results
