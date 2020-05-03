from abc import ABCMeta, abstractmethod

from nose.tools import eq_, assert_raises

from cipher import CaesarShiftCipher, VigenereCipher

PANGRAM = "Sphinx of black quartz, judge my vow!"


class BaseTestCase(metaclass=ABCMeta):
    @abstractmethod
    def test_uppercase_encipher(self):
        pass

    @abstractmethod
    def test_lowercase_encipher(self):
        pass

    @abstractmethod
    def test_uppercase_decipher(self):
        pass

    @abstractmethod
    def test_lowercase_decipher(self):
        pass

    @abstractmethod
    def test_encipher_non_alphabetic_characters(self):
        pass

    @abstractmethod
    def test_decipher_non_alphabetic_characters(self):
        pass


class TestCaesarShiftCipher(BaseTestCase):
    def test_uppercase_encipher(self):
        cipher_suite = CaesarShiftCipher(5)
        eq_(cipher_suite.encipher("CIPHER"), "HNUMJW")

        cipher_suite = CaesarShiftCipher(25)
        eq_(cipher_suite.encipher("AMZ"), "ZLY")

    def test_lowercase_encipher(self):
        cipher_suite = CaesarShiftCipher(5)
        eq_(cipher_suite.encipher("cipher"), "HNUMJW")

        cipher_suite = CaesarShiftCipher(25)
        eq_(cipher_suite.encipher("amz"), "ZLY")

    def test_encipher_non_alphabetic_characters(self):
        eq_(
            CaesarShiftCipher(13).encipher(PANGRAM),
            "FCUVAK BS OYNPX DHNEGM, WHQTR ZL IBJ!",
        )

    def test_uppercase_decipher(self):
        cipher_suite = CaesarShiftCipher(5)
        eq_(cipher_suite.decipher("HNUMJW"), "CIPHER")

        cipher_suite = CaesarShiftCipher(25)
        eq_(cipher_suite.decipher("ZLY"), "AMZ")

    def test_lowercase_decipher(self):
        cipher_suite = CaesarShiftCipher(5)
        eq_(cipher_suite.decipher("hnumjw"), "CIPHER")

        cipher_suite = CaesarShiftCipher(25)
        eq_(cipher_suite.decipher("zly"), "AMZ")

    def test_decipher_non_alphabetic_characters(self):
        eq_(
            CaesarShiftCipher(13).decipher("FCUVAK BS OYNPX DHNEGM, WHQTR ZL IBJ!"),
            PANGRAM.upper(),
        )

    def test_invalid_shift(self):
        with assert_raises(ValueError):
            CaesarShiftCipher(-1)

        with assert_raises(ValueError):
            CaesarShiftCipher(26)


class TestVigenereCipher(BaseTestCase):
    def test_uppercase_encipher(self):
        cipher_suite = VigenereCipher("LEMON")
        eq_(cipher_suite.encipher("ATTACK"), "LXFOPV")

    def test_lowercase_encipher(self):
        cipher_suite = VigenereCipher("lemon")
        eq_(cipher_suite.encipher("attack"), "LXFOPV")

    def test_uppercase_decipher(self):
        cipher_suite = VigenereCipher("LEMON")
        eq_(cipher_suite.decipher("LXFOPV"), "ATTACK")

    def test_lowercase_decipher(self):
        cipher_suite = VigenereCipher("lemon")
        eq_(cipher_suite.decipher("lxfopv"), "ATTACK")

    def test_encipher_non_alphabetic_characters(self):
        cipher_suite = VigenereCipher(PANGRAM)
        eq_(cipher_suite.encipher(PANGRAM), "KEOQAU TG BNKSE HNZANC, VSYUA BF ILK!")

    def test_decipher_non_alphabetic_characters(self):
        cipher_suite = VigenereCipher(PANGRAM)
        eq_(
            cipher_suite.decipher("KEOQAU TG BNKSE HNZANC, VSYUA BF ILK!"),
            PANGRAM.upper(),
        )

    def test_empty_key(self):
        with assert_raises(ValueError):
            VigenereCipher("")

        with assert_raises(ValueError):
            VigenereCipher("123!")
