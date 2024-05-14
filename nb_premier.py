#!/usr/bin/env python3

print("Nombre premier")

nb=input('Donnez un nombre : ')
nbdiv=0
for i in range(1, int(nb)+1):
    if int(nb)%i==0:
        nbdiv=nbdiv+1

if nbdiv==2:
    print('{0} : est un nombre premier'.format(nb))
else:
    print('{0} : n\'est pas un nombre premier'.format(nb))
