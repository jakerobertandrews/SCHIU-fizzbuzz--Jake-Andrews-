# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:03:29 2019

@author: Jake
"""

import unittest

from FizzBuzz_v2 import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
      
    def test_values(self):
        self.assertRaises(ValueError, fizzbuzz, -2)
        self.assertRaises(ValueError, fizzbuzz, 0)
        
    def test_types(self):
        self.assertRaises(TypeError, fizzbuzz, 3+4j)
        self.assertRaises(TypeError, fizzbuzz, True)
        self.assertRaises(TypeError, fizzbuzz, "String")

if __name__ == '__main__':
    unittest.main()

    
    