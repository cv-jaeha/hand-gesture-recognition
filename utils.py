# Import Library
from pynput.keyboard import Key, Controller
import time


class TestKeyboard:
    def __init__(self):
        self.keyboard = Controller()

    def inputKey(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)

    def inputKeyWithShift(self, key):
        with self.keyboard.pressed(Key.shift):
            self.keyboard.press(key)
            self.keyboard.release(key)

    def inputKeyWithControl(self, key):
        with self.keyboard.pressed(Key.ctrl):
            self.keyboard.press(key)
            self.keyboard.release(key)

    def inputKeyWith(self, with_key, key):
        with self.keyboard.pressed(with_key):
            self.keyboard.press(key)
            self.keyboard.release(key)

    def typeString(self, string):
        self.keyboard.type(string)


kb = TestKeyboard()


def close_ridi():
    kb.inputKeyWith(Key.alt_l, Key.f4)
    time.sleep(1)
    kb.inputKeyWith(Key.alt_l, Key.f4)
    time.sleep(1)


def next_page():
    kb.inputKey(Key.right)
    time.sleep(1)


def prev_page():
    kb.inputKey(Key.left)
    time.sleep(1)