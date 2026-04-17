# Data Structures and Algorithms (DSA) - Midterm Project

##  Project Overview
This project provides a comprehensive technical analysis of Array time and space optimization, aiming to approach numerous problems in the most efficient way. It focuses on advanced algorithmic paradigms: **Prefix Sum, Sliding Window, Difference Array, and Core Array operations**.

It combines theory foundations, time and space complexity analysis, and real-world problem-solving applications.

### **Main Contents**
- **Research & Implementation**  
  Implemented both from scratch (custom classes) and using Python built-in features for:
  - Prefix Sum  
  - Sliding Window  
  - Difference Array  
  - Dynamic Array  

- **Analysis & Optimization**  
  Detailed evaluation of Big-O complexity, mathematical foundations, and decision-making strategies ("What to use") for different problem types.

- **Practice & Synthesis**  
  Solved LeetCode problems, analyzed real-world applications, and summarized all concepts through LaTeX reports with visual diagrams.

---

## Team Members

| Full Name | Student ID | Contribution |
|----------|------------|-------------|
| Le Pham Khanh Linh | [Student ID] | -- |
| Tran Viet Long | [Student ID] | -- |
| Vu Tran Cat Linh | [Student ID] | -- |
| Phung Nhat Minh | [Student ID] | -- |

---

##  Project Structure

```text
dsa/
│
├── Leetcode/
│   ├── Array_resize.ipynb
│   ├── Difference_array.ipynb
│   └── Prefix_sum.ipynb
|   └── Sliding_window.ipynb
│
├── built_in/
│   ├── difference_array.py
│   ├── prefix_sum.py
│   ├── sliding_window.py
│   
│
├── src/
│   ├── array.py
│   ├── difference_array.py
│   ├── prefix_sum.py
│   └── sliding_window.py
│
├── test_built_in/
│   ├── __init__.py
│   ├── test_difference_array.py
│   ├── test_prefix_sum.py
│   └── test_sliding_window.py
│
├── tests/
│   ├── __init__.py
│   ├── test_array.py
│   ├── test_difference_array.py
│   ├── test_prefix_sum.py
│   └── test_sliding_window.py
│
├── .gitignore
└── requirements.txt
```
## Project Roadmap and Workflow

The development of this project follows a structured workflow to ensure both theoretical depth and practical implementation:

### 1. Concept Selection & Understanding
- Select core data structures and techniques
- Identify key concepts, strengths, weaknesses
- Compare with alternative approaches

### 2. Research & Theoretical Foundation
- Study references (CLRS, GeeksforGeeks, etc.)
- Develop detailed report outline
- Write **Theory & Concepts**, including:
  - Core principles
  - Mathematical foundations
  - Complexity analysis
  - **“What to use” mindset** (choosing the right technique for each problem)

### 3. Complexity Analysis
- Analyze Big-O for all operations
- Build comparison tables:
  - Insert / Delete / Peek / Search
  - Across different implementations

### 4. Implementation
- Implement from scratch using Python (no external libraries)
  - Clean class design
  - Docstrings
  - Basic test cases
- Implement versions using Python built-in features

### 5. Applications & Problem Solving
- Research 3–4 real-world applications:
  - Problem description
  - Why the technique fits
- Solve 4–5 problems (LeetCode / HackerRank):
  - Mix of Easy & Medium
  - Provide detailed explanations:
    - Intuition
    - Algorithm
    - Complexity
    - Code

### 6. Visualization & Documentation
- Add diagrams:
  - Data structure visualization
  - Operation flows (insert / update / query)
- Label all figures clearly
- Integrate real-world applications into report

### 7. Finalization
- Compile full report using LaTeX
- Write README
- Write Introduction & Conclusion
- Test all code (ensure no bugs)
- Final review and refinement

## Installation Guide
### Step 1: Clone the repository
git clone [https://github.com/khanhlinh170806-cpu/dsa.git](https://github.com/khanhlinh170806-cpu/dsa.git)

### Step 2: Navigate to the project directory
cd dsa

### Step 3: Create a virtual environment (recommended)
python -m venv venv

### BStep 4: Activate the virtual environment
### On Windows:
venv\Scripts\activate
### On macOS/Linux:
source venv/bin/activate

### Step 5: Install dependencies
pip install -r requirements.txt

## How to Run
### Run all tests
pytest tests/

### Run a specific file
python src/tên_file.py

## Technologies Used
Language: Python
Formats: .py, .ipynb (Jupyter Notebook for explanations)
Testing: Pytest (unit testing framework)
