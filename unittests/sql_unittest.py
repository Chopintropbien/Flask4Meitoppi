__author__ = 'andrei'

import unittest
from source.SQLengine import session, generate_example_usr, andrei_dict

class MyTestCase(unittest.TestCase):

    def test_creation(self):
        generate_example_usr(andrei_dict)
        session.commit()
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
