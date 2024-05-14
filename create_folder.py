import os

def creer_dossier(dossiers):
    for key, values in dossiers.items():
        for value in values:
            dossier='{0}/{1}/{2}'.format(base,key,value)
            os.makedirs(dossier)
            print('creation du dossier {0}'.format(dossier))


base = '/home/bmy/Desktop/Structure'
#base = base.replace('/', '-')
#print(base)

structure =   {
            'Musique':['Rock', 'Jazz', 'Pop'],
            'Documents':['Facture', 'Travail', 'Maison'],
            'Image':['Vaccances', 'Famille'],
            'Videos':['Amimaux', 'Rire']
            }

creer_dossier(structure)
