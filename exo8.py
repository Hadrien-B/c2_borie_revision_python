note_eleves = {
    "Lisa": "18",
    "Hugo": "17",
    "Romain": "12",
    "Flo": "20",
    "Lola": "19",
    "Ines": "14",
    "Will": "20",
}
meilleur_eleve = max(note_eleves, key=note_eleves.get)
meilleure_note = note_eleves[meilleur_eleve]

print("L'élève avec la meilleure note est",
      meilleur_eleve, "avec une note de", meilleure_note)
