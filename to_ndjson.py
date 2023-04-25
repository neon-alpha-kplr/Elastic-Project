"""
        Ouvrir le fichier et Charger les données JSON à partir du fichier
        Créer une liste vide pour stocker les données à envoyer à Elasticsearch
        
        Pour chaque document dans les données JSON :
            Créer une action de type "index" pour chaque document
            Ajouter l'action à la liste des données
            Ajouter le document à la liste des données
            
        Ajouter un caractère de nouvelle ligne à la fin de la requête
        Écrire les données dans un fichier .ndjson
"""
import json
import os

path='.'

for fn in os.listdir(path):
    if fn[-5:]=='.json':
        print(f"Processing file {fn}...")
        fp=os.open(fn, 'r')
        json.load(fp)
        os.close(fp)
