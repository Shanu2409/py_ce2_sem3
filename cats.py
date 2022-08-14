import imp
import requests
from PIL import Image
import os

def generate():
    url = 'https://cataas.com/cat'
    filename = './post/cat.jpg'

    r = requests.get(url)

    with open(filename, 'wb') as f:
        f.write(r.content)
        return filename

# generate()