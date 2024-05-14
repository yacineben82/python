#!/usr/bin/env python3
import random, time, string

mdp = input("Entrez un mot de passe : ")

def mot_aleatoire():
    lettres = string.ascii_letters
    suivant = ""
    resultat = ""
    for i in range(len(mdp)):
        while mdp[i] != suivant:
            print(resultat + suivant)
            suivant = random.choice(lettres)
        resultat = resultat + suivant
    return resultat

debut = time.time()
print(mot_aleatoire())
print("Duree : " + str((time.time() - debut)) + "secondes")
