import file_process as fp
from typing import Dict, Callable, List, Union


class HotKey:
    def __init__(self, key: Union[str, List[str]] = "", command=""):
        self.key = key
        self.command_name = command

    @property
    def command_name(self) -> str:
        return self._command_name

    @command_name.setter
    def command_name(self, command: str) -> None:
        self._command_name = command

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, key: Union[str, List[str]]) -> None:
        if type(key) == str:
            self._key = key
        else:
            self._key = HotKey.from_list(key)

    @staticmethod
    def from_list(keys: List[str]) -> str:
        new_keys = [f"<{key}>" if len(key) > 1 else key for key in keys]
        return "+".join(new_keys)

    def __str__(self):
        return self.key + " --- " + self.command_name

    def __repr__(self):
        return str(self)


class KeyMapper:
    def __init__(self):
        self.maps: Dict[str, List[HotKey]] = {}
        self.active_map_name: str = ""

    @staticmethod
    def from_file(file_name: str) -> "KeyMapper":
        return fp.read(file_name)

    def write(self, file_name: str) -> None:
        fp.write(file_name, self)

    def keys(self, map_name: str) -> List[HotKey]:
        return self.maps[map_name]

    def map(self, map_name: str, hotkeys: List[HotKey]) -> None:
        self.maps[map_name] = hotkeys

    def active_keys(self):
        return self.keys(self.active_map_name)

    def connect(self, func: Dict[str, Callable]) -> Dict[HotKey, Callable]:
        keys = self.active_keys()
        connected_hotkeys: Dict[HotKey, Callable] = {}
        for key in keys:
            connected_hotkeys[key] = func[key.command_name]
        return connected_hotkeys

# k = KeyMapper()
# for name in "default", "my", "custom":
#     l = []
#     for i in range(5):
#         l.append(HotKey(f"{name[0]}+{i}", f"{name[0]}{i}"))
#     k.map(name, l.copy())
#
# print(k.maps)
# k.active_map_name = "default"
# k.write("keys.json")
