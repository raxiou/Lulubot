def stat_hero(data):
    '''cette fonction vas recuperer dans le donné du personage les stat(sous forme de dico toujours)'''
    for i in range(len(data) - 1):
        return data["results"][i]["calculatedStatus"]["lv50FiveStarFullyAwakened"]


def imprint_hero(data):
    '''cette fonction vas recuperer dans le donné du personage l'imprint'(sous forme de dico toujours)'''
    for i in range(len(data) - 1):
        return data["results"][i]["devotion"]


def skills(data):
    '''cette fonction vas recuperer dans le donné du personage les skills(sous forme de dico toujours)'''
    for i in range(len(data) - 1):
        return data["results"][i]["skills"]
