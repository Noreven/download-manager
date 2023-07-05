from pathlib import Path


path_mapping = {".jpg": Path(r"C:\Users\HP\OneDrive - Bit srl\Immagini")}


def get_path(ext: str):
    return path_mapping.get(ext, None)


def add_path(ext: str, path: Path):
    path_mapping.update({"ext": path})
