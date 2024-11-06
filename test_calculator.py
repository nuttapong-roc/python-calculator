import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1,2),3)
        self.assertEqual(self.calc.add(5,7),12)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2,3),-1)
        self.assertEqual(self.calc.subtract(10,9),1)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(20,3),60)
        self.assertEqual(self.calc.multiply(50,100),5000)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,2),0)
        self.assertEqual(self.calc.modulo(21,5),1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()