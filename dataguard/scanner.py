import re
from .regex_patterns import PATTERNS

def scan_file(path):
    results = []

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for lineno, line in enumerate(f, start=1):
                for label, pattern in PATTERNS.items():
                    matches = re.findall(pattern, line)
                    for match in matches:
                        results.append({
                            "type": label,
                            "match": match,
                            "file": path,
                            "line": lineno
                        })
    except Exception as e:
        print(f"[!] Error leyendo {path}: {e}")
    
    return results
