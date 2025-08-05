import os
import argparse
from dataguard.utils import list_text_files
from dataguard.scanner import scan_file

def main():
    parser = argparse.ArgumentParser(description="Escanea archivos en busca  de datos sensibles")
    parser.add_argument("path", help="Ruta a la directorio o fichero a escanear")
    args = parser.parse_args()

    results = []

    if os.path.isfile(args.path):
        results.extend(scan_file(args.path))
    else:
        files = list_text_files(args.path)
        for file in files:
            results.extend(scan_file(file))
            
    if results:
        print("\n[+] Posibles datos sensibles encontrados:")
        for r in results:
            print(f"[{r['type']}] {r['match']} - {r['file']} (línea {r['line']})")
    else:
        print("[!] No se encontraron datos sensibles.")

if __name__ == "__main__":
    main()
