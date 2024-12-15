import unittest
from encodings.punycode import selective_find
from math import sin, cos, sqrt, floor, ceil
from tkinter import Tk
from main import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.calc = Calculator(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_addition(self):
        self.calc.expression = "2+3"
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.result_var.get(), "5")

    def test_subtraction(self):
        self.calc.expression = "5-2"
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.result_var.get(), "3")

    def test_multiplication(self):
        self.calc.expression = "3*4"
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.result_var.get(), "12")

    def test_division(self):
        self.calc.expression = "10/2"
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.result_var.get(), "5.0")

    def test_sin_function(self):
        self.calc.expression = "0"
        self.calc.on_button_click('sin')
        self.assertEqual(self.calc.result_var.get(), str(sin(0)))

    def test_cos_function(self):
        self.calc.expression = "0"
        self.calc.on_button_click('cos')
        self.assertEqual(self.calc.result_var.get(), str(cos(0)))

    def test_square_root(self):
        self.calc.expression = "4"
        self.calc.on_button_click('√')
        self.assertEqual(self.calc.result_var.get(), str(sqrt(4)))

    def test_floor_function(self):
        self.calc.expression = "3.7"
        self.calc.on_button_click('floor')
        self.assertEqual(self.calc.result_var.get(), str(floor(3.7)))

    def test_ceil_function(self):
        self.calc.expression = "3.2"
        self.calc.on_button_click('ceil')
        self.assertEqual(self.calc.result_var.get(), str(ceil(3.2)))

    def test_memory_add(self):
        self.calc.expression = "5"
        self.calc.on_button_click('m+')
        self.calc.on_button_click('mc')
        self.assertEqual(self.calc.memory, 0)

    def test_clear(self):
        self.calc.expression = "5+3"
        self.calc.on_button_click('C')
        self.assertEqual(self.calc.result_var.get(), "")

    def test_null_dev(self):
        self.calc.expression= "5/0"
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.result_var.get(), "Error")

    def test_letter(self):
        self.calc.expression = "~!@#$%^&*()имтавгшмаовш"
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.result_var.get(), "Error")

    def test_incorrect_placement(self):
        self.calc.expression = "*5++4"
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.result_var.get(), "Error")

if __name__ == "main":
    unittest.main()