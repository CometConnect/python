import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"\n{event.src_path} has been created")

    def on_deleted(self, event):
        print(f"\n{event.src_path} has been deleted")

    def on_moved(self, event):
        print(f"\n{event.src_path} has been moved")

    def on_modified(self, event):
        print(f"\n{event.src_path} has been modified")


event_handler = Handler()
observer = Observer()
observer.schedule(
    event_handler,
    os.getcwd()
)
observer.start()

try:
    while True:
        time.sleep(2)
        print(".", end="")
except KeyboardInterrupt:
    print("!")
    observer.stop()
