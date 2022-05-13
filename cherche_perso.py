import json

def cherche_persoE7(hero):
    with open('BDD/bddE7/bddE7.json','r', encoding='utf-8') as monFichier:
        data = json.load(monFichier)
        
    for dico in data:
        if dico['nom'].upper() == hero.upper():
            return dico
    return False
            
def cherche_perso_Genshin(hero):
    with open(f'BDD/bddGenshin/{hero}.json','r', encoding='utf-8') as monFichier:
        data = json.load(monFichier)        
    return data