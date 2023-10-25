import csv

nom_fichier = input(
    "Entrez le nom du fichier à analyser (avec l'extension .csv) : ")

with open(nom_fichier, 'r') as fichier:
    contenu = fichier.read()
    mots = contenu.split()
    nombre_de_mots = len(mots)

nom_fichier_csv = 'resultat.csv'
with open(nom_fichier_csv, 'w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(['Nombre de mots dans le fichier', nombre_de_mots])

print(f"Le nombre de mots a été compté et écrit dans '{nom_fichier_csv}'.")
