# PDC_exec

PDC TIER 1 ASSIGNMENT Name = Hamza Shahab roll number = 21b-214-cs

# Parallel vs Serial Processing Assignment

This repository demonstrates the comparison between serial processing and parallel processing using Python for a data processing task involving student and fee data.

# Objective

To implement and compare the performance of serial computation and multiprocessing-based parallel computation for processing large datasets. This assignment highlights the benefits of parallel processing in reducing execution time for computationally intensive tasks.

# Dataset

# Files Used:

1. **students.csv:** Contains a list of students with their IDs, names, and major.**
2. **student_fees.csv:** Contains fee payment details, including student IDs, amounts, and payment dates.

# Sample Data:

**students.csv**

![image](https://github.com/user-attachments/assets/6b61317c-8c18-4480-a52e-3cfa7c830f1d)

**fees.csv**

![image](https://github.com/user-attachments/assets/189a81db-a04b-4227-a3ff-3d23e597ce23)

# Scripts

# 1. Serial Computation (serial_computation.py)
  1.This script processes the data sequentially using pandas.
  
  2.Iterates through each student record and matches it with relevant fee payment dates from the fees dataset.
  
  3.Calculates the frequency of fee payment dates using a dictionary.
  
  4.Result
  
  ![image](https://github.com/user-attachments/assets/a9568ce5-f351-4739-9022-095544536c66)

  5.**Execution Time:** 146.1819 seconds

# 2. Parallel Computation (multiprocessing_computation.py)
  1.This script processes the data using Python's multiprocessing module.
  2.Distributes the processing of student records across multiple CPU cores to reduce computation time.
  3.Also calculates the frequency of fee payment dates using dictionaries, but in parallel.

  ![image](https://github.com/user-attachments/assets/6fbf809b-5ebe-412c-8192-8210b22bc7e5)

  4.**Execution Time:** 12.4577 seconds.
