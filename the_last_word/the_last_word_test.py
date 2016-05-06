import unittest
import the_last_word

class TestTheLastWord(unittest.TestCase):

  def test_1(self):
      self.assertEqual(the_last_word.extract_last_word("CAB"), "CAB")
      self.assertEqual(the_last_word.extract_last_word("JAM"), "MJA")
      self.assertEqual(the_last_word.extract_last_word("CODE"), "OCDE")
      self.assertEqual(the_last_word.extract_last_word("ABAAB"), "BBAAA")
      self.assertEqual(the_last_word.extract_last_word("CABCBBABC"), "CCCABBBAB")
      self.assertEqual(the_last_word.extract_last_word("ABCABCABC"), "CCCBAABAB")
      self.assertEqual(the_last_word.extract_last_word("ZXCASDQWE"), "ZXCASDQWE")


if __name__ == '__main__':
    unittest.main()
