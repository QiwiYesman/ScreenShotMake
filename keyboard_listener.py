from typing import Dict, Callable

import pynput_robocorp.keyboard as keyboard


class KeyboardListener:
    def __init__(self):
        self.listener = keyboard.Listener()
        self._hotkeys = {}

    @property
    def hotkeys(self) -> Dict[str, Callable]:
        return self._hotkeys

    @hotkeys.setter
    def hotkeys(self, hotkeys: Dict[str, Callable]) -> None:
        self._hotkeys = hotkeys
        # self.set_finish_hotkey()

    def set_finish_hotkey(self) -> None:
        self.hotkeys["<alt>+j"] = self.stop

    def reset(self) -> None:
        self.hotkeys = {}
        self.stop()

    def stop(self) -> None:
        if self.listener.running:
            self.listener.stop()

    def start(self) -> None:
        if self.listener.running:
            self.stop()
        self.listener = keyboard.GlobalHotKeys(self.hotkeys)
        self.listener.start()
