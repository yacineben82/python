#!/usr/bin/env python3

print("Nombre pair ou impair")

nb=input("Donnez un nombre : ")

if int(nb)%2==0:
    print("le nombre {0} est pair".format(nb))
else:
    print("le nombre {0} est impair".format(nb))
