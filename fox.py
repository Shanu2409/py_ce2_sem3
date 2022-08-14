from urllib import response
import requests

response = requests.get("https://randomfox.ca/floof")
fox = response.json()
url = (fox['image'])

filename = './post/fox.jpg'

r = requests.get(url)

def generate():
    with open(filename, 'wb') as f:
        f.write(r.content)
    return filename