from pathlib import Path
from typing import Tuple, List


class Folder:
    def __init__(self, folder: str = ""):
        self.folder = folder

    @property
    def folder(self) -> Path:
        if self._folder:
            return self._folder.resolve()
        return Path("NO PATH")

    @folder.setter
    def folder(self, folder: str) -> None:
        if Path(folder).is_dir():
            self._folder = Path(folder)
        else:
            self._folder = ""

    def _get_full_path(self, file: str) -> Path:
        return self._folder / file

    def exists(self, file: str) -> bool:
        return self._get_full_path(file).is_file()

    @staticmethod
    def split_by_ext(file: str) -> Tuple[str, str]:
        p = Path(file)
        return p.stem, str.join('', p.suffixes)

    @staticmethod
    def extensions(file: str) -> List[str]:
        return Path(file).suffixes

    @staticmethod
    def name(file: str) -> str:
        return Path(file).stem

    def get_unique_fullpath(self, file: str) -> str:
        i = 0
        name, suffixes = self.split_by_ext(file)
        while self.exists(f"{name}_{i}{suffixes}"):
            i += 1
        return str(self._get_full_path(f"{name}_{i}{suffixes}"))

    def create(self, relative_folder_path: str) -> "Folder":
        new_path = self.folder / relative_folder_path
        if not new_path.exists():
            Path.mkdir(new_path)
        return Folder(str(new_path))
