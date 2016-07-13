import unittest
import numbers_in_list

class TestNumbersInList(unittest.TestCase):

  def test_addONE(self):
      self.assertEqual(numbers_in_list.add_ONE([],1), [1]) 
      self.assertEqual(numbers_in_list.add_ONE([1],1), [2]) 
      self.assertEqual(numbers_in_list.add_ONE([2],1), [3]) 
      self.assertEqual(numbers_in_list.add_ONE([1,2],1), [1,3]) 
      self.assertEqual(numbers_in_list.add_ONE([9],1), [1,0]) 
      self.assertEqual(numbers_in_list.add_ONE([7,9],1), [8,0]) 


  def test_add_generic_nr(self):
      self.assertEqual(numbers_in_list.add_generic_nr([],1), [1]) 
      self.assertEqual(numbers_in_list.add_generic_nr([1],1), [2]) 
      self.assertEqual(numbers_in_list.add_generic_nr([2],1), [3]) 
      self.assertEqual(numbers_in_list.add_generic_nr([1,2],1), [1,3]) 
      self.assertEqual(numbers_in_list.add_generic_nr([9],1), [1,0]) 
      self.assertEqual(numbers_in_list.add_generic_nr([7,9],1), [8,0]) 
      self.assertEqual(numbers_in_list.add_generic_nr([7,9],5), [8,4]) 
      self.assertEqual(numbers_in_list.add_generic_nr([9,9,9],9), [1,0,0,8]) 

if __name__ == '__main__':
    unittest.main()
