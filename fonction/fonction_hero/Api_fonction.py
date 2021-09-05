import requests
def get_api(hero):
    '''la fonction vas chercher toute les donné sur un personnage dans l'api "epicsevendb"
    et les recupere sous forme de dictionnaire'''

    #l'api est bien faite il suffie d'ajouter le nom du hero a la fin du lien pour avoir accé a ces donnés
    api_url = ("https://api.epicsevendb.com/hero/" + hero)

    #on fait la requete a l'api
    reponse = requests.get(api_url)

    #si l'api a bien recu la requette mettre ok dans la console et transformer se qu'on a recu en dictionnaire puis le retourner
    if reponse.status_code == 200:
        print("ok")
        contenu = reponse.json()
        return contenu
    #sinon ne rien retourner et ecrire dans la console "pas bon
    else:
        print("pas bon")
        return False