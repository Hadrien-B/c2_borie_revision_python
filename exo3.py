def addition_utilisateur(nombre1, nombre2):
    return nombre1 + nombre2

def soustraction_utilisateur(nombre1, nombre2):
    return nombre1 - nombre2

def multiplication_utilisateur(nombre1, nombre2):
    return nombre1 * nombre2

def division_utilisateur(nombre1, nombre2):
    if nombre2 == 0:
        return "Division par zéro!"
    return nombre1 / nombre2

nombre1 = float(input("Tapez votre premier nombre ici : "))
nombre2 = float(input("Tapez votre deuxième nombre ici : "))

resultat_addition = addition_utilisateur(nombre1, nombre2)
resultat_soustraction = soustraction_utilisateur(nombre1, nombre2)
resultat_multiplication = multiplication_utilisateur(nombre1, nombre2)
resultat_division = division_utilisateur(nombre1, nombre2)

print("Résultat de l'addition : " + str(resultat_addition))
print("Résultat de la soustraction : " + str(resultat_soustraction))
print("Résultat de la multiplication : " + str(resultat_multiplication))
print("Résultat de la division : " + str(resultat_division))
