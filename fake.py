from urllib import request

img = "http://picsum.photos/200"

def generate():
    request.urlretrieve(img, "./post/img.jpg")
    return "./post/img.jpg"