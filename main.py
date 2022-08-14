# import schedular as sc
import cats as c
import app as post
import schedule as sc
import time


def run():
    c.generate()
    post.post()

# run()
# sc.every().day.at("20:46").do(run)
# sc.every(60).seconds.do(run)

# while (True):
#     sc.run_pending()
#     time.sleep(10)

run()

time.sleep(10)