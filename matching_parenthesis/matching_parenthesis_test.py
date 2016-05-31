import unittest
from matching_parenthesis import *

class TestMatchingParenthesis(unittest.TestCase):
    def test_isCorrent(self):
        self.assertEqual(isBalanced(""), True)
        self.assertEqual(isBalanced("()"), True)
        self.assertEqual(isBalanced("("), False)
        self.assertEqual(isBalanced("(({}))[]"), True)
        self.assertEqual(isBalanced("(({})[]"), False)
        self.assertEqual(isBalanced("(({})(a+b))[]"), True)
        self.assertEqual(isBalanced(")()"), False)

    def test_recIsBalanced(self):
        self.assertEqual(recIsBalanced(""), True)
        self.assertEqual(recIsBalanced("()"), True)
        self.assertEqual(recIsBalanced("("), False)
        self.assertEqual(recIsBalanced("(({}))[]"), True)
        self.assertEqual(recIsBalanced("(({})[]"), False)
        self.assertEqual(recIsBalanced(")()"), False)
        self.assertEqual(recIsBalanced("(())))"), False)




if __name__ == '__main__':
    unittest.main()
