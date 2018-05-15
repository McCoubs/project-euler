# Project-Euler

- This project is inspired by [Project-Euler](https://projecteuler.net/)
- Each of the subsequent sub-directories contains a possible solution in python (v. 3.6.5) to one of the Project-Euler questions

# Directory Files

All directories contain up to 4 files:
  - `name_of_func.py`: which is main logical solution behind each of the project's questions, all directories will contain this file
  - `main.py`: which is the command line runner for each solution
  - `tests.py`: which contains the unit tests for each sub-directory, run each file to run each problems related tests

# Running All Tests

- navigate to main directory and run: `python -m unittest discover . tests.py`