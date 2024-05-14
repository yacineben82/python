#!/usr/bin/env python3

print("Extension de fichier")

import os

chemin=input('Donnez le chemin du fichier : ')

if os.path.exists(chemin):
    ext=chemin.split(".")
    print("l\'extension du fichier est : ." + ext[-1])
else:
    print('le fichier n\'existe pas')
