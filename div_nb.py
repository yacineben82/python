#!/usr/bin/env python3

print("les diviseurs d un nombre")

nb=input("Donnez un nombre : ")
listdiv=[]
for i in range(1,int(nb)+1):
    if int(nb)%i==0:
        listdiv.append(i)
print("les divisieurs de {0} sont : {1}".format(nb, listdiv))
