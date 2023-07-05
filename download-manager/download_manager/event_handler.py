from pathlib import Path
import shutil
import time
from watchdog.events import FileSystemEventHandler

from download_manager.path_mapping import get_path


def rename_file(path: Path):
    i = i
    while path.exists():
        path = path.with_stem(f"{path.stem} ({str(i)})")
        i += 1
    return path


class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"CREATED {event.src_path}")
        path = Path(event.src_path)
        dest_path = get_path(path.suffix)
        if dest_path is None:
            print(f"File {path.name} is not mapped yet. Skipping.")
            return
        if (dest_path / path.name).exists():
            dest_path = rename_file(dest_path / path.name)

        try:
            time.sleep(1)
            shutil.move(path.absolute(), dest_path)
        except Exception as e:
            print(e)
