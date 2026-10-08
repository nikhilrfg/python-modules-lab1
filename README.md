# Python Lab 1 - Modules, Packages, and PIP

## Overview

This lab demonstrates how to use Python built-in modules, create and import
a custom module inside a package, and install and use external packages
with PIP.

---

## Task 1 - Built-in Modules

The `builtin_usage.py` program uses the following built-in Python modules:

- `math`
- `random`
- `platform`

The program generates a random number between 1 and 100, calculates its
square root and rounds it down, and displays information about the
operating system and Python version.

### Example Output

```text
Random Number: 77
Square Root (floored): 8
Operating System: Windows
Python Version: 3.14.7
```

---

## Task 2 - Custom Module and Package

The `mypackage` folder contains:

- `utilities.py`
- `__init__.py`

The `utilities.py` module contains two functions:

- `greet(name)` - Returns a greeting message.
- `factorial(n)` - Calculates and returns the factorial of a number.

The `use_utilities.py` program imports the module using:

```python
from mypackage import utilities
```

### Example Output

```text
Hello, Nikhil! Welcome!
Factorial of 5: 120
```

---

## Task 3 - External Packages

For this task, I used two external Python packages:

- `colorama`
- `requests`

They can be installed using PIP:

```text
python -m pip install colorama
python -m pip install requests
```

### Colorama

The `external_package.py` program uses Colorama to display colored text
in the terminal.

### Example Output

```text
Hello from Colorama!
Python modules are fun!
This text is back to the normal color.
```

### Requests

The `requests_example.py` program uses the Requests package to send an
HTTP GET request to a website and display the HTTP status code.

### Example Output

```text
HTTP Status Code: 200
```

A status code of `200` means that the HTTP request was successful.

---

## Project Structure

```text
python-modules-lab1/
│
├── builtin_usage.py
├── external_package.py
├── requests_example.py
├── use_utilities.py
├── README.md
│
└── mypackage/
    ├── __init__.py
    └── utilities.py
```

---

## What I Learned

In this lab, I learned how to import and use built-in Python modules such
as `math`, `random`, and `platform`.

I also learned how to create my own module, organize it inside a Python
package using `__init__.py`, and import functions from that package into
another Python program.

Finally, I learned how to use PIP to install third-party packages. I used
Colorama to display colored terminal text and Requests to send an HTTP
request to a website and retrieve its status code.