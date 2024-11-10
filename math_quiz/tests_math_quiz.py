import unittest
from math_quiz import function_A, function_B, function_C

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        """Test if random numbers generated are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Value {rand_num} out of range!")

    def test_function_B(self):
        """Test if the random operator generated is one of the specified operators."""
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random operator generations
            operator = function_B()
            self.assertIn(operator, valid_operators, f"Invalid operator {operator} generated.")

    def test_function_C(self):
        """Test if function_C returns correct problem strings and answers."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 3, '+', '10 + 3', 13),
            (10, 3, '-', '10 - 3', 7),
            (10, 3, '*', '10 * 3', 30)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Problem string incorrect for {num1} {operator} {num2}")
            self.assertEqual(answer, expected_answer, f"Answer incorrect for {num1} {operator} {num2}")

if __name__ == "__main__":
    unittest.main()
