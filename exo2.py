phrase_utilisateur = input("Tapez votre phrase: ")
phrase_minuscule = phrase_utilisateur.lower()
phrase_majuscule = phrase_utilisateur.upper()
nombre_de_mots = len(phrase_utilisateur.split())

print("la phrase est:" + phrase_minuscule)
print("la phrase est:" + phrase_majuscule)
print("Le nombre de mots dans la phrase : ", nombre_de_mots)

