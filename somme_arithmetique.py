#!/usr/bin/env python3

print("la valeur de la somme de 1+2+....nb")
s=0
nb=input("Donnez un nombre : ")

for i in range(int(nb)+1):
    s=s+i
print("la valeur de la somme est " + str(s))
