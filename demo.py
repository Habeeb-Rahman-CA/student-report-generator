"""Demo script illustrating data handling and basic statistics concepts."""

from report_generator import (
    calculate_mean,
    calculate_median,
    print_report,
)


def demonstrate_concepts():
    print("=" * 60)
    print("   LEARNING: BASIC STATISTICS & DATA HANDLING (NO THEORY)   ")
    print("=" * 60)

    # 1. Data Handling: Raw Data
    marks = [45, 88, 32, 91, 74, 38, 62]
    students = ["Sam", "Priya", "John", "Ananya", "Leo", "Meera", "Carlos"]

    print("\n1. DATA HANDLING:")
    print(f"   Raw marks list   : {marks}")
    print(f"   Sorted marks list: {sorted(marks)}")
    print(f"   Total records    : {len(marks)}")

    # 2. Statistics: Mean vs Median
    mean_val = calculate_mean(marks)
    median_val = calculate_median(marks)

    print("\n2. STATISTICS (IN SIMPLE TERMS):")
    print(f"   • Mean (Average) = Sum / Count = {sum(marks)} / {len(marks)} = {mean_val:.2f}")
    print("     (Gives a single summary number for the overall performance)")
    print(f"   • Median (Middle Value) = {median_val:.2f}")
    print("     (Gives the middle score that separates top 50% from bottom 50%)")

    # 3. Pass / Fail Evaluation & Report
    print("\n3. REPORT OUTPUT:")
    print_report(
        title="Midterm Examination Report",
        marks=marks,
        names=students,
        passing_threshold=40.0,
    )


if __name__ == "__main__":
    demonstrate_concepts()

