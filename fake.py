from urllib import request
import resize as re

img = "http://picsum.photos/200"

def generate():
    request.urlretrieve(img, "./post/img.jpg")
    re.resize("./post/img.jpg")
    return "./post/img.jpg"