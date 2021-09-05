import random


def creation_tableau(Liste_joueur):
    nombre_de_joueurs = len(Liste_joueur)
    matchs = []
    for i in range(int(len(Liste_joueur)/2)):
        Duel = []
        for i in range(2):
            joueur = random.choice(Liste_joueur)
            Liste_joueur = [e for e in Liste_joueur if e not in (joueur)]
            Duel.append(joueur)
        matchs.append(Duel)

    print(len(matchs))
    if nombre_de_joueurs % 2 == 1:
        Liste_joueur.append('Le Pape')
        matchs.append(Liste_joueur)
    print(matchs)

    return matchs


