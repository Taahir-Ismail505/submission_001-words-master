import unittest
from unittest.mock import patch
from word_processor import convert_to_word_list ,words_lengths_map,letters_count_map, most_used_character, words_longer_than
from io import StringIO

class MyTestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(convert_to_word_list("These are indeed interesting, an obvious understatement, times. What say you?"),
        ['these', 'are', 'indeed', 'interesting', 'an', 'obvious', 'understatement', 'times', 'what', 'say', 'you'])
    
    def test2(self):
        self.assertEqual(words_longer_than(10,"These are indeed interesting, an obvious understatement, times. What say you?"),['interesting','understatement'])

    def test3(self):
        self.assertEqual(words_lengths_map("These are indeed interesting, an obvious understatement, times. What say you?"),{2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1})
    
    def step4(self):
        self.assertEqual(letters_count_map("These are indeed interesting, an obvious understatement, times. What say you?"),{'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2,
             'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0})
    def step5(self):
        self.assertEqual(most_used_character({'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2,
             'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}),'e')
    
    def step6(self):
       self.assertIsNone(most_used_character(""),None)