#!/usr/bin/env python3

print("table de multiplication")

rep='o'
i=0

while rep == 'o':
    nb=input('Donner un nomnre : ')
    print('la table de multiplication de : ' + nb)
    for i in range(11):
        print('{0} X {1} = {2}'.format(nb, i, int(nb) * i))
    rep = input('Voulez vous continuer ? o/n : ')
