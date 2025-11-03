# Modules and Packages: Exercises

## 1. Math Operations Package

### 1. Create a Package

- Create a package named `src`.
- Inside the `src` package, create a module named `math_operations`.
- Define functions `add`, `subtract`, `multiply`, and `divide` in the `math_operations` module that perform the respective operations on two numbers and return the result.

### 2. Import and Use Module

- Create a new Python script named `math_analysis.py` outside the `src` package (hint: this needs to be in the same root folder as `src`).
- Import the functions from `src.math_operations`.
- Use each function with sample numbers.
- Print the results.
- Execute `math_analysis.py` as a script to see the printed results.

### 3. Conditional Execution

- Add a conditional statement in `src.math_operations` to print a message `"src.math_operations is being executed directly."` when the module is executed as a directly.
- Test this out by executing it directly vs executing it via a import (i.e the latter will mean you have to execute `math_analysis.py` directly.)

## 2. Data Processing Package *

### 1. Create a Data Processing Package

- Create a package named `data_processing` with a module named `cleaning`.
Within the `cleaning` module, define a function named `remove_duplicates` that takes a list as input and returns a new list with duplicates removed (with order preserved).

### 2. Import and Use Cleaning Module

- Create a new Python script named `data_analysis.py` outside the `data_processing` package. Within this script, create a sample list with duplicated values and use the function defined in step 1 to create a cleaned version of the list.
- Print the cleaned list to verify correctness.

### 3. Extend the Package

- Add a new module named `transforming` to the `data_processing` package. This module should have a function named `capitalise_strings` that takes a list of strings as input and returns the same list with all strings capitalised.
- Modify the `data_analysis.py` by creating a sample list of strings. Use the newly created function and mutate your sample list of strings.
- Print the transformed list to verify correctness.

### 4. Conditional Execution

- Add a conditional statement to the `cleaning.py` module that prints a message when the module is executed directly.
- Ensure that the message is only printed when the module is run directly and not when it's imported into another script.
- Test the behavior by running the `cleaning.py` module directly and importing it into the `data_analysis.py` script.

### 5. Use Package-Level Imports

- Make both `capitalise_strings` and `remove_duplicates` package-level functions.
- Modify the `data_analysis.py` and use both functions now as package level functions.
