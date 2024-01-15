import sys
import time
import random
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"Directory created: {event.src_path}")
        else:
            print(f"File created: {event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
            print(f"Directory modified: {event.src_path}")
        else:
            print(f"File modified: {event.src_path}")

    def on_moved(self, event):
        if event.is_directory:
            print(f"Directory moved: {event.src_path} to {event.dest_path}")
        else:
            print(f"File moved: {event.src_path} to {event.dest_path}")

    def on_deleted(self, event):
        if event.is_directory:
            print(f"Directory deleted: {event.src_path}")
        else:
            print(f"File deleted: {event.src_path}")

if __name__ == "__main__":
    from_dir = "/Users/luannabuco/Downloads"
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, from_dir, recursive=True)
    observer.start()

    print(f"Watching for file system events in: {from_dir}")
    print("Press any key to stop the observer.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

