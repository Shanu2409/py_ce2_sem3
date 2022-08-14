from urllib import request

img = "http://picsum.photos/200"
request.urlretrieve(img, "./post/img.jpg")