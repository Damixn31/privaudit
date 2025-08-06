import os
import argparse
from dataguard.utils import list_text_files, load_rules
from dataguard.scanner import scan_file
from colorama import init, Fore, Style

def main():
    init()
    parser = argparse.ArgumentParser(description="\tEscanea archivos en busca de datos sensibles")
    parser.add_argument("path", help="Ruta a un archivo o directorio")
    args = parser.parse_args()

    rules = load_rules("dataguard/rules.json")
    results = []

    if os.path.isfile(args.path):
        results.extend(scan_file(args.path, rules))
    elif os.path.isdir(args.path):
        files = list_text_files(args.path)
        for file in files:
            results.extend(scan_file(file, rules))
    else:
        print(Fore.RED + "[!] Ruta inválida." + Style.RESET_ALL)
        return 

    if results:
        print(Fore.GREEN + "\n[+] Datos sensibles encontrados:\n" + Style.RESET_ALL)
        for r in results:
            
            print(
                f"\t{Fore.MAGENTA} [{r['type']}]" 
                f"{Fore.WHITE} {r['match']} |" 
                f"{Fore.GREEN} Ruta: {r['file']} |" 
                f"{Fore.RED} Línea: {r['line']}"
                f"{Style.RESET_ALL}\n")
    else:
        print(Fore.RED + "\n[!] No se encontraron datos sensibles.\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
