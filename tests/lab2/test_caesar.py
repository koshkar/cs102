import unittest 
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar("ILOVEBEER"), 'LORYHEHHU')
        self.assertEqual(encrypt_caesar("bruuuuuuh"), 'euxxxxxxk')
        self.assertEqual(encrypt_caesar("9mm"), '9pp')
        self.assertEqual(encrypt_caesar(""), '')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar("LORYHEHHU"), 'ILOVEBEER')
        self.assertEqual(decrypt_caesar("euxxxxxxk"), 'bruuuuuuh')
        self.assertEqual(decrypt_caesar("9pp"), '9mm')
        self.assertEqual(decrypt_caesar(""), '')

if __name__ == '__main__':
    unittest.main()
