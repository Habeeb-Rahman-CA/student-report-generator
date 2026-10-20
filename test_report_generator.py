import unittest
from report_generator import (
    calculate_mean,
    calculate_median,
    is_pass,
    parse_marks_input,
    generate_class_report,
)


class TestStudentReportGenerator(unittest.TestCase):

    def test_calculate_mean(self):
        # Normal case
        self.assertAlmostEqual(calculate_mean([10, 20, 30]), 20.0)
        # Decimal marks
        self.assertAlmostEqual(calculate_mean([50.5, 60.5]), 55.5)
        # Single element
        self.assertAlmostEqual(calculate_mean([75]), 75.0)
        # Empty list
        self.assertEqual(calculate_mean([]), 0.0)

    def test_calculate_median_odd_length(self):
        # Odd number of items: middle element after sorting
        self.assertEqual(calculate_median([70, 10, 90]), 70.0)
        self.assertEqual(calculate_median([5, 1, 9, 3, 7]), 5.0)

    def test_calculate_median_even_length(self):
        # Even number of items: average of middle two
        # Sorted: [10, 20, 30, 40] -> (20 + 30) / 2 = 25.0
        self.assertEqual(calculate_median([40, 10, 30, 20]), 25.0)
        self.assertEqual(calculate_median([80, 90]), 85.0)

    def test_calculate_median_empty(self):
        self.assertEqual(calculate_median([]), 0.0)

    def test_is_pass(self):
        # Default threshold is 40
        self.assertTrue(is_pass(40))
        self.assertTrue(is_pass(40.1))
        self.assertTrue(is_pass(99))
        self.assertFalse(is_pass(39.9))
        self.assertFalse(is_pass(0))

        # Custom threshold
        self.assertTrue(is_pass(50, passing_threshold=50))
        self.assertFalse(is_pass(49.5, passing_threshold=50))

    def test_parse_marks_input(self):
        input_str = "85, 92; 38  105 -5 abc 70"
        # 105, -5, abc should be ignored
        parsed = parse_marks_input(input_str)
        self.assertEqual(parsed, [85.0, 92.0, 38.0, 70.0])

    def test_generate_class_report(self):
        students = [
            {"name": "Alice", "mark": 80},
            {"name": "Bob", "mark": 35},
            {"name": "Charlie", "mark": 65},
        ]
        result = generate_class_report(students, passing_threshold=40.0)

        self.assertEqual(result["total_students"], 3)
        self.assertEqual(result["passed_count"], 2)
        self.assertEqual(result["failed_count"], 1)
        self.assertAlmostEqual(result["mean"], 60.0)
        self.assertAlmostEqual(result["median"], 65.0)
        self.assertAlmostEqual(result["pass_rate"], 66.67)


if __name__ == "__main__":
    unittest.main()

