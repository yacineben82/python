#!/usr/bin/env python3

print('nombre d\'occurrence de caractere')

s=input('Donnez une chaine de caractere : ')

for c in s:
    print('le caractere : {0} figure {1} fois dans la chaine s'.format(c, s.count(c)))
