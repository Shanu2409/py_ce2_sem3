from urllib import response
import requests

response = requests.get("https://meme-api.herokuapp.com/gimme/wholesomememes/2")
meme = response.json()
url = (meme['url'])

filename = './post/meme2.png'

r = requests.get(url)

with open(filename, 'wb') as f:
    f.write(r.content)