import json
import requests

def get_api(hero):
    #récupère les donnée de l'api
    api_url = ("https://api.epicsevendb.com/hero/" + hero)

    reponse = requests.get(api_url)

    if reponse.status_code == 200:
        print("ok")
        contenu = reponse.json()
        return contenu
    else:
        print("pas bon")
        return False
  
  

with open('bddE7.json', encoding= 'utf-8') as monFichier:
    donnée = json.load(monFichier)
    
data = get_api('alexa')

for i in range(len(data) - 1):
    donnée_grade = data["results"][i]['self_devotion']['grades']


print(donnée['self_devotion']['grade'])
donnée['self_devotion']['grade']['SSS'] = donnée_grade['SSS']
print(donnée['self_devotion']['grade'])

with open('bddE7.json', 'w', encoding= 'utf-8') as mon_fichier:
    json.dump(donnée, mon_fichier)
    
