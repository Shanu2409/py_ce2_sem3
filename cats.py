import imp
import requests
from PIL import Image
import os
import resize as re

def generate():
    url = 'https://cataas.com/cat'
    filename = './post/cat.jpg'

    r = requests.get(url)

    with open(filename, 'wb') as f:
        f.write(r.content)
    re.resize(filename)
    return filename
    

# generate()