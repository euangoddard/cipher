import re
from abc import ABCMeta, abstractmethod

A_CODE_POINT = ord("A")


class BaseCipher(metaclass=ABCMeta):

    _known_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encipher(self, value: str) -> str:
        chars_enciphered = []
        for pos, char in enumerate(value.upper()):
            if char in self._known_chars:
                chars_enciphered.append(self.encipher_char(char, pos))
            else:
                chars_enciphered.append(char)

        return "".join(chars_enciphered)

    def decipher(self, value: str) -> str:
        chars_deciphered = []
        for pos, char in enumerate(value.upper()):
            if char in self._known_chars:
                chars_deciphered.append(self.decipher_char(char, pos))
            else:
                chars_deciphered.append(char)

        return "".join(chars_deciphered)

    @abstractmethod
    def encipher_char(self, char: str, pos: int) -> str:
        pass

    @abstractmethod
    def decipher_char(self, char: str, pos: int) -> str:
        pass


class CaesarShiftCipher(BaseCipher):
    def __init__(self, shift: int):
        if shift < 0 or 25 < shift:
            raise ValueError("shift must in the range 0-25 inclusive")
        self.shift = shift

    def encipher_char(self, char: str, pos: int) -> str:
        return chr(
            A_CODE_POINT
            + (ord(char) + self.shift - A_CODE_POINT) % len(self._known_chars)
        )

    def decipher_char(self, char: str, pos: int) -> str:
        return chr(
            A_CODE_POINT
            + (ord(char) - self.shift - A_CODE_POINT) % len(self._known_chars)
        )


class VigenereCipher(BaseCipher):

    _NON_LETTER_RE = re.compile(r"[^A-Z]")

    def __init__(self, key: str):
        self.key = "".join(self._NON_LETTER_RE.split(key.upper()))
        if not self.key:
            raise ValueError("Key must be non-empty and contain at least one letter!")

    def encipher_char(self, char: str, pos: int) -> str:
        shift = self._get_shift_for_position(pos)
        if shift == 0:
            return char
        else:
            caesar_shift_cipher = CaesarShiftCipher(shift)
            return caesar_shift_cipher.encipher_char(char, pos)

    def decipher_char(self, char: str, pos: int) -> str:
        shift = self._get_shift_for_position(pos)
        if shift == 0:
            return char
        else:
            caesar_shift_cipher = CaesarShiftCipher(shift)
            return caesar_shift_cipher.decipher_char(char, pos)

    def _get_shift_for_position(self, pos: int) -> int:
        index = pos % len(self.key)
        char = self.key[index]
        return ord(char) - A_CODE_POINT
