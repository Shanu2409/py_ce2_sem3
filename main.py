import cats as c
import app as post
import time
import fox as f
import meme as meme
import fake as fake
import random


def select():
    num = round(random.randint(0,3))
    if num == 0:
        return c.generate() #cat
    elif num == 1:
        return f.generate() #fox
    elif num == 2:
        return fake.generate() #fake
    elif num == 3:
        return meme.generate() #meme

def run():
    post.post(select())



run()

time.sleep(5)