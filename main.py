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
        return c.generate()
    elif num == 1:
        return f.generate()
    elif num == 2:
        return fake.generate()
    elif num == 3:
        return meme.generate()

def run():
    # f.generate()
    post.post(select())



run()

time.sleep(5)