from urllib import response
import requests

response = requests.get("https://meme-api.herokuapp.com/gimme/wholesomememes")
meme = response.json()
url = (meme['url'])

filename = './post/meme.png'

r = requests.get(url)

def generate():
    with open(filename, 'wb') as f:
        f.write(r.content)
        return filename