from instabot import Bot
import os 
import shutil
shutil.rmtree(r'./config')

bot = Bot()
user = 'deadshort2020'
pas = 'pass@777'
text = 'first post!!!!'

def post(img = './post/meme.jpg'):
    # cookie_del = glob.glob("config/*cookie.json")
    # os.remove(cookie_del)

    src = img
    des = "./posted_img"
    shutil.copy(src, des)

    bot.login(username=user, password=pas)
    bot.upload_photo(img, caption='thanks')
    img = img + '.REMOVE_ME'
    os.remove(img)

post("./post/img.jpg")