import unittest
from greet import greeter



class test_greeter(unittest.TestCase):


    def test_greeter_output_with_valid_name(self):
        self.assertEqual(greeter('kacsa'), 'Hello, kacsa!')

    def test_greeter_output_without_name(self):
        self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

if __name__ == '__main__':
    unittest.main()
