import unittest
import counting_sheep

class TestStringMethods(unittest.TestCase):

  def test_1(self):
      self.assertEqual(counting_sheep.last_nr_seen(1), 10)
      self.assertEqual(counting_sheep.last_nr_seen(2), 90)
      self.assertEqual(counting_sheep.last_nr_seen(5), 90)
      self.assertEqual(counting_sheep.last_nr_seen(11), 110)
      self.assertEqual(counting_sheep.last_nr_seen(1692), 5076)
      self.assertEqual(counting_sheep.last_nr_seen(0), "INSOMNIA")


if __name__ == '__main__':
    unittest.main()
