def main():
    # ressourcen-Zugriff in Python mit automatischem Schließen der Ressource, bevorzugte Variante
    with open('README.md', 'r') as opened_file: 
        rows = opened_file.readlines()
        for row in rows:
            print(row)

main()
