import unittest

def normalToRomanNumbers(number, romanNumber=""):
    defaultNumbers = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}


    if(defaultNumbers.has_key(number)):
        romanNumber += defaultNumbers[number]
    else:
        defaultNrDecrement = sorted(defaultNumbers)
        defaultNrDecrement.reverse()
        if(number > 5):
            for i, nr in enumerate(defaultNrDecrement):
                if number%nr < number:
                    romanNumber += defaultNumbers[defaultNrDecrement[i]]
                    return normalToRomanNumbers(number-nr, romanNumber)

        while(number > 0):
            romanNumber += "I"
            number -= 1

    return romanNumber



def romanToNormalNumbers(romanNumber):
    resultNumber = 0

    defaultNumbers = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}

    i=0
    while(i<len(romanNumber)-1):
        ch = romanNumber[i]
        next_ch = romanNumber[i+1]
        if defaultNumbers.has_key( ch + next_ch ):
            resultNumber += defaultNumbers[ch + next_ch]
            i += 2
        elif defaultNumbers.has_key( ch ):
            resultNumber += defaultNumbers[ch]
            i += 1
        else:
            resultNumber = "NOT VALID"
            break

    if(i < len(romanNumber) and defaultNumbers.has_key(romanNumber[i])):
        resultNumber += defaultNumbers[romanNumber[i]] #add last number

    return resultNumber



class MyTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(normalToRomanNumbers(0), "")

    def test_default(self):
        self.assertEqual(normalToRomanNumbers(1), "I")
        self.assertEqual(normalToRomanNumbers(5), "V")
        self.assertEqual(normalToRomanNumbers(10), "X")
        self.assertEqual(normalToRomanNumbers(50), "L")
        self.assertEqual(normalToRomanNumbers(100), "C")
        self.assertEqual(normalToRomanNumbers(1000), "M")

        self.assertEqual(romanToNormalNumbers("I"), 1)
        self.assertEqual(romanToNormalNumbers("V"), 5)
        self.assertEqual(romanToNormalNumbers("X"), 10)
        self.assertEqual(romanToNormalNumbers("L"), 50)
        self.assertEqual(romanToNormalNumbers("C"), 100)
        self.assertEqual(romanToNormalNumbers("M"), 1000)

    def test_lessThanFive(self):
        self.assertEqual(normalToRomanNumbers(2), "II")
        self.assertEqual(normalToRomanNumbers(3), "III")

        self.assertEqual(romanToNormalNumbers("II"), 2)
        self.assertEqual(romanToNormalNumbers("III"), 3)

    def test_lessThanTen(self):
        self.assertEqual(normalToRomanNumbers(6), "VI")
        self.assertEqual(normalToRomanNumbers(7), "VII")
        self.assertEqual(normalToRomanNumbers(8), "VIII")

        self.assertEqual(romanToNormalNumbers("VI"), 6)
        self.assertEqual(romanToNormalNumbers("VII"), 7)
        self.assertEqual(romanToNormalNumbers("VIII"), 8)

    def test_bigNumbers(self):
        self.assertEqual(normalToRomanNumbers(1990), "MCMXC")
        self.assertEqual(normalToRomanNumbers(2008), "MMVIII")
        self.assertEqual(normalToRomanNumbers(2000), "MM")

        self.assertEqual(romanToNormalNumbers("MCMXC"), 1990)
        self.assertEqual(romanToNormalNumbers("MMVIII"), 2008)
        self.assertEqual(romanToNormalNumbers("MM"), 2000)

    def test_notValidInput(self):
        self.assertEqual(romanToNormalNumbers("MAA"), "NOT VALID")


if __name__ == '__main__':
    unittest.main()
