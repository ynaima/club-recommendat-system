"""A3. Test cases for function club_functions.get_last_to_first.
"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_one_person_mult_friend_same_last(self):
        param = {'Jesse Katsopolis': ['Danny R Katsopolis', 'Joey Katsopolis',
                            'Rebecca Katsopolis']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Katsopolis':['Danny R', 'Jesse', 'Joey', 'Rebecca']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
        
        


if __name__ == '__main__':
    unittest.main(exit=False)
