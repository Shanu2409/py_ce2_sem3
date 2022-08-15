import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import posting as p

class Watcher:

    def __init__(self, directory="./img_file", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")


class MyHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)
        src = event.src_path
        p.posting(src)

if __name__=="__main__":
    w = Watcher(".", MyHandler())
    w.run()