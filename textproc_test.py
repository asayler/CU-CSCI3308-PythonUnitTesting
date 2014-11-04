#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.text = "abc123"
        self.p = textproc.Processor(text)

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.p.text, self.text, "'text' does not match input")
    
    def test_init_number(self):
       self.assertRaises(TypeError,  textproc.Processor, (3))
    
    def test_count_alpha(self):
        self.assertEqual(self.p.count_alpha(), 3)
        
    def test_count_vowels(self):
        self.assertEqual(self.p.count_vowels(), 1)
    
    def test_count_numeric(self):
        self.assertEqual(self.p.count_numeric(), 3)
    
    def test_is_phonenumber(self):
        self.assertFalse(textproc.Processor(2).is_phonenumber())
        self.assertTrue(textproc.Processor("303-740-6061"))

    # Add Your Test Cases Here...

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
