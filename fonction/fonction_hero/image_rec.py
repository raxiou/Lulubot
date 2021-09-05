def image_recup(data):

    for i in range(len(data) - 1):
        image = data["results"][i]["assets"]["image"]

    return image