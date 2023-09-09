# file to test swap_name.py

import unittest
import swap_name

class TestSwapName(unittest.TestCase):
  
   def test_swap_name(self):
      name = 'John Smith'
      expected = 'Smith, John'
      self.assertEqual(swap_name.swap_name(name), expected)

if __name__ == '__main__':
   unittest.main()
   