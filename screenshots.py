import pyscreenshot as ps
import PIL.Image

class Screenshot:

    @staticmethod
    def screenshot(area: tuple, backend: str) -> PIL.Image.Image:
        return ps.grab(bbox=area, backend=backend, childprocess=False)

    @staticmethod
    def save(image: PIL.Image.Image, path: str) -> None:
        image.save(path)

    @staticmethod
    def screenshot_save(area: tuple, backend: str, path: str) -> None:
        Screenshot.save(Screenshot.screenshot(area, backend), path)
