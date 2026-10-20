"""Student Report Generator.

Concepts learned:
1. Basic Statistics (no heavy theory):
   - Mean (Average): Total sum divided by count of items.
   - Median (Middle Value): Value right in the center when numbers are sorted.
2. Data Handling:
   - Input validation (handling invalid numbers, ranges 0-100).
   - Transforming lists and dictionaries into structured reports.
"""

from typing import List, Dict, Union, Tuple, Optional


def calculate_mean(marks: List[Union[int, float]]) -> float:
    """Calculate the arithmetic mean (average) of a list of marks.

    How it works:
    Add all marks together, then divide by how many marks there are.
    """
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def calculate_median(marks: List[Union[int, float]]) -> float:
    """Calculate the median (middle value) of a list of marks.

    How it works:
    1. Sort numbers from lowest to highest.
    2. If odd count: pick the exact middle number.
    3. If even count: take the average of the two middle numbers.
    """
    if not marks:
        return 0.0

    sorted_marks = sorted(marks)
    n = len(sorted_marks)
    mid = n // 2

    # Odd number of elements -> pick the middle one
    if n % 2 == 1:
        return float(sorted_marks[mid])

    # Even number of elements -> average of two middle values
    return (sorted_marks[mid - 1] + sorted_marks[mid]) / 2.0


def is_pass(mark: Union[int, float], passing_threshold: float = 40.0) -> bool:
    """Determine whether a mark passes or fails based on a threshold."""
    return mark >= passing_threshold


def parse_marks_input(raw_input: str) -> List[float]:
    """Clean and convert user input string into a list of valid float marks.

    Supports comma, space, or semicolon separated numbers.
    Example: '85, 90, 78' -> [85.0, 90.0, 78.0]
    """
    # Replace commas and semicolons with spaces for simple splitting
    cleaned = raw_input.replace(",", " ").replace(";", " ")
    tokens = cleaned.split()

    marks: List[float] = []
    for token in tokens:
        try:
            val = float(token)
            if 0.0 <= val <= 100.0:
                marks.append(val)
            else:
                print(f"Warning: Skipping {val} (marks must be between 0 and 100)")
        except ValueError:
            print(f"Warning: Skipping '{token}' (not a valid number)")
    return marks


def generate_class_report(
    students: List[Dict[str, Union[str, float]]],
    passing_threshold: float = 40.0,
) -> Dict[str, Union[float, int, List[Dict[str, Union[str, float, str]]]]]:
    """Generate overall summary statistics and student-level pass/fail status."""
    if not students:
        return {
            "mean": 0.0,
            "median": 0.0,
            "total_students": 0,
            "passed_count": 0,
            "failed_count": 0,
            "pass_rate": 0.0,
            "students": [],
        }

    marks = [float(s["mark"]) for s in students]
    mean_val = calculate_mean(marks)
    median_val = calculate_median(marks)

    detailed_students = []
    passed_count = 0

    for s in students:
        name = str(s["name"])
        mark = float(s["mark"])
        passed = is_pass(mark, passing_threshold)
        if passed:
            passed_count += 1
        detailed_students.append({
            "name": name,
            "mark": mark,
            "status": "PASS" if passed else "FAIL",
        })

    failed_count = len(students) - passed_count
    pass_rate = (passed_count / len(students)) * 100.0

    return {
        "mean": round(mean_val, 2),
        "median": round(median_val, 2),
        "total_students": len(students),
        "passed_count": passed_count,
        "failed_count": failed_count,
        "pass_rate": round(pass_rate, 2),
        "students": detailed_students,
    }


def print_report(
    title: str,
    marks: List[float],
    names: Optional[List[str]] = None,
    passing_threshold: float = 40.0,
) -> None:
    """Print an aesthetically formatted text report."""
    if not marks:
        print(f"\n--- {title} ---")
        print("No marks provided.\n")
        return

    mean_val = calculate_mean(marks)
    median_val = calculate_median(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)

    print("\n" + "=" * 50)
    print(f" {title.center(48)} ")
    print("=" * 50)

    # Student-wise breakdown
    print(f"{'No.':<5}{'Student / Item':<25}{'Mark':<10}{'Status':<10}")
    print("-" * 50)

    passed_count = 0
    for idx, mark in enumerate(marks, start=1):
        name = names[idx - 1] if names and idx - 1 < len(names) else f"Student {idx}"
        status = "PASS" if is_pass(mark, passing_threshold) else "FAIL"
        if status == "PASS":
            passed_count += 1
        print(f"{idx:<5}{name:<25}{mark:<10.1f}{status:<10}")

    total = len(marks)
    failed_count = total - passed_count
    pass_percentage = (passed_count / total) * 100.0

    print("-" * 50)
    print("STATISTICAL SUMMARY:")
    print(f"  • Total Entries : {total}")
    print(f"  • Mean (Average): {mean_val:.2f}")
    print(f"  • Median (Middle): {median_val:.2f}")
    print(f"  • Highest Mark  : {highest_mark:.1f}")
    print(f"  • Lowest Mark   : {lowest_mark:.1f}")
    print("-" * 50)
    print("RESULT BREAKDOWN:")
    print(f"  • Passing Mark  : {passing_threshold:.1f}")
    print(f"  • Passed        : {passed_count}")
    print(f"  • Failed        : {failed_count}")
    print(f"  • Pass Rate     : {pass_percentage:.1f}%")
    print("=" * 50 + "\n")


def main() -> None:
    """Interactive CLI runner for the Student Report Generator."""
    print("=== Student Report Generator ===")
    print("Enter student marks separated by spaces or commas (e.g. 78, 45, 92, 33, 60)")
    user_input = input("Enter marks: ").strip()

    if not user_input:
        print("No input provided. Running with sample data instead:")
        sample_marks = [85.0, 42.0, 38.0, 95.0, 67.0, 73.0, 29.0]
        sample_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace"]
        print_report("Sample Classroom Report", sample_marks, sample_names)
        return

    marks = parse_marks_input(user_input)
    if not marks:
        print("No valid marks were parsed. Exiting.")
        return

    threshold_input = input("Enter passing mark threshold [Default: 40]: ").strip()
    passing_threshold = 40.0
    if threshold_input:
        try:
            passing_threshold = float(threshold_input)
        except ValueError:
            print("Invalid threshold entered. Using default (40).")

    print_report("Student Performance Report", marks, passing_threshold=passing_threshold)


if __name__ == "__main__":
    main()

