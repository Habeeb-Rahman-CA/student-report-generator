# Student Report Generator

A clean, beginner-friendly Python application that takes student marks as input and generates an analytical summary report.

---

## 🎯 What You Learn

### 1. Basic Statistics (No Complex Theory)
* **Mean (Average):**
  * *What it is:* Add all marks together and divide by how many students there are.
  * *Why we use it:* Gives one representative number for the overall performance of the whole group.
  * *Example:* `[40, 60, 80]` $\rightarrow (40 + 60 + 80) / 3 = 60.0$
* **Median (Middle Value):**
  * *What it is:* Sort all numbers from lowest to highest and pick the one right in the middle (or average the two middle numbers if the count is even).
  * *Why we use it:* Unlike the mean, the median is not skewed by a single unusually high or low score (outlier).
  * *Example (Odd):* `[30, 45, 95]` $\rightarrow$ sorted is `[30, 45, 95]` $\rightarrow$ middle is `45.0`
  * *Example (Even):* `[20, 40, 60, 80]` $\rightarrow$ middle two are 40 and 60 $\rightarrow (40 + 60) / 2 = 50.0$
* **Pass / Fail Logic:**
  * Compares each student's score against a passing benchmark (default: 40%).
  * Calculates pass count, fail count, and the overall pass rate percentage.

### 2. Data Handling
* **Data Ingestion & Cleaning:**
  * Accepting varied input formats (comma-separated, space-separated, semicolon-separated).
  * Filtering out invalid strings and keeping numbers within the valid range ($0 \le \text{mark} \le 100$).
* **Data Transformation:**
  * Converting raw user text into numeric lists (`float`).
  * Mapping marks to structured records (dictionaries) with computed attributes like `status` ("PASS" / "FAIL").
* **Output Formatting:**
  * Rendering aligned tables and structured summary statistics.

---

## 🚀 Quick Start

### 1. Run the Demo
Demonstrates data handling and shows both odd/even calculations:
```bash
python3 demo.py
```

### 2. Run Interactively
Run the interactive report generator to input custom marks:
```bash
python3 report_generator.py
```
*Example input:*
```text
Enter marks: 78, 45, 92, 33, 60, 84
Enter passing mark threshold [Default: 40]: 40
```

### 3. Run Unit Tests
```bash
python3 -m unittest test_report_generator.py
```

---

## 📂 Project Structure

- [`report_generator.py`](file:///home/habrmnc/habrmnc/student-report-generator/report_generator.py): Core logic for calculating mean, median, pass/fail thresholds, input parsing, and report display.
- [`demo.py`](file:///home/habrmnc/habrmnc/student-report-generator/demo.py): Walkthrough showing raw data handling and statistics in action.
- [`test_report_generator.py`](file:///home/habrmnc/habrmnc/student-report-generator/test_report_generator.py): Automated test suite for mean, median (odd and even lengths), input sanitization, and pass/fail logic.

