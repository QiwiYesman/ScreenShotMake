from dataclasses import dataclass
import file_process as fp


@dataclass
class DefaultStruct:
    default_path: str = ""
    default_image_name: str = ""
    default_image_ext: str = ""
    default_is_paused: bool = False
    default_after_screen_defining: bool = False
    default_backend: str = ""

    @property
    def values(self):
        return (
            self.default_path,
            self.default_image_name,
            self.default_image_ext,
            self.default_is_paused,
            self.default_after_screen_defining,
            self.default_backend
        )

    @values.setter
    def values(self, values: list):
        for key, value in zip(self.__dict__.keys(), values):
            self.__dict__[key] = value

    @staticmethod
    def from_file(file_name: str) -> 'DefaultStruct':
        return fp.read(file_name)

    def save(self, file_name: str) -> None:
        fp.write(file_name, self)

    def __repr__(self):
        return str(self.values)
