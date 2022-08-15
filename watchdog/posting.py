from instabot import Bot
import os

bot = Bot()

user = 'deadshort2020'
pas = 'pass@777'
text = 'first post!!!!'

bot.login(username=user, password=pas)


def posting(src):
    bot.upload_photo(src, caption='form src')
    try:
        dl = src + '.REMOVE_ME'
        os.remove(dl)
    except:
        pass
    print("done posting....")