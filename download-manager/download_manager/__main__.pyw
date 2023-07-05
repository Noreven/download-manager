import time
from watchdog.observers import Observer

from download_manager.event_handler import DownloadHandler


def main():
    folder_path = r"C:\Users\HP\Downloads"
    observer = Observer()
    observer.schedule(DownloadHandler(), folder_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
