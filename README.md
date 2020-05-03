# Caesar Shift and Vigenère cipher implementations

An implementation of the Caesar Shift and Vigenère ciphers in Python

## Installation

In a Virtualenv (or Docker, etc.) running Python 3.7 or above, run

```bash
$ pip install -r requirements.txt
```

## Usage

Import and yse the cipher(s) you want in your IDLE:

```pycon
>>> from cipher import CaesarShiftCipher, VigenereCipher                                                                                                                                                                                   
>>> caesar_5 = CaesarShiftCipher(5)                                                                                                                                                                                                        
>>> caesar_5.encipher("Sphinx of black quartz, judge my vow!")                                                                                                                                                                             
'XUMNSC TK GQFHP VZFWYE, OZILJ RD ATB!'
>>> caesar_5.decipher('XUMNSC TK GQFHP VZFWYE, OZILJ RD ATB!')                                                                                                                                                                             
'SPHINX OF BLACK QUARTZ, JUDGE MY VOW!'
>>> vigenere_lemon = VigenereCipher('LEMON')                                                                                                                                                                                               
>>> vigenere_lemon.encipher('Sphinx of black quartz, judge my vow!')                                                                                                                                                                      
'"WBVVYB CS FXOPV CINCXL, UYPUR QK IZA!'
>>> vigenere_lemon.decipher('WBVVYB CS FXOPV CINCXL, UYPUR QK IZA!')                                                                                                                                                                      
'SPHINX OF BLACK QUARTZ, JUDGE MY VOW!'
```

## Tests

Run the tests with `nose`:

```bash
$ nosetests test_cipher.py
```