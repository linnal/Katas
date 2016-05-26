import unittest
import ceaser_chiper

class TestCeaserChiper(unittest.TestCase):

    def test_encrypt_char(self):
        cc = ceaser_chiper.CeaserChiper(3)
        self.assertEqual(cc.encrypt_char(""), "")
        self.assertEqual(cc.encrypt_char("A"), "D")
        self.assertEqual(cc.encrypt_char("a"), "")
        self.assertEqual(cc.encrypt_char("Z"), "C")
        self.assertEqual(cc.encrypt_char("X"), "A")
        return

    def test_encrypt(self):
        cc = ceaser_chiper.CeaserChiper(3)
        self.assertEqual(cc.encrypt(""), "")
        self.assertEqual(cc.encrypt("AZ"), "DC")
        self.assertEqual(cc.encrypt("AaZ"), "DC")

    def test_descrypt_char(self):
        cc = ceaser_chiper.CeaserChiper(3)
        self.assertEqual(cc.descrypt_char(""), "")
        self.assertEqual(cc.descrypt_char("D"), "A")
        self.assertEqual(cc.descrypt_char("A"), "X")
        self.assertEqual(cc.descrypt_char("B"), "Y")
        self.assertEqual(cc.descrypt_char("C"), "Z")

    def test_descrypt(self):
        cc = ceaser_chiper.CeaserChiper(3)
        self.assertEqual(cc.descrypt(""), "")
        self.assertEqual(cc.descrypt("DC"), "AZ")

    def test_encrypt_char_shift_5(self):
        cc = ceaser_chiper.CeaserChiper(5)
        self.assertEqual(cc.encrypt_char("A"), "F")
        self.assertEqual(cc.encrypt_char("X"), "C")

    def test_descrypt_char_shift_5(self):
        cc = ceaser_chiper.CeaserChiper(5)
        self.assertEqual(cc.descrypt_char("F"), "A")
        self.assertEqual(cc.descrypt_char("C"), "X")


if __name__ == '__main__':
    unittest.main()
