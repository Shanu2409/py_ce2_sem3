

def say():
    print("Hello shanu")

def says():
    print("Hello sunny")

sc.every(3).seconds.do(say)
# sc.every().day.at("19:22").do(says)

while (True):
    sc.run_pending()
    time.sleep(1)
