#!/usr/bin/env python3

print("Calcul du factoriel")


nb=input("Donnez un nombre : ")
p=1
for i in range(1,int(nb)+1):
    p=p*i
print("le factoriel de {0} est : {1}".format(nb, p))
