from instabot import Bot
import os 
import shutil
shutil.rmtree(r'./config')

bot = Bot()
user = 'deadshort2020'
pas = 'pass@777'
text = 'first post!!!!'

def post(img = ''):
    
    # cookie_del = glob.glob("config/*cookie.json")
    # os.remove(cookie_del)

    # src = img
    # des = "./posted_img"
    # shutil.copy(src, des)

    try:
        bot.login(username=user, password=pas)
        bot.upload_photo(img, caption='thanks')
        img = img + '.REMOVE_ME'
        os.remove(img)
    except:
        print("ERROR!!!!!!!!!!!")

def post_folder(src):
    bot.login(username=user, password=pas)

    for file in os.listdir(src):
        bot.upload_photo(src + "/" + file, caption= '#happy')
        # os.remove(src)
        try:
            dl = src + "/" + file + '.REMOVE_ME'
            os.remove(dl)
        except:
            pass

# post("./post/img.jpg")
# post_folder("./post")