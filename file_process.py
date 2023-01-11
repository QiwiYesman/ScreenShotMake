from typing import Any

import jsonpickle


def read(file_name: str) -> Any:
    with open(file_name, 'r') as file:
        return jsonpickle.decode(file.read())


def write(file_name: str, obj: Any) -> None:
    with open(file_name, 'w') as file:
        file.write(jsonpickle.encode(obj))
