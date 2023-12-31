# Near Earth Objects Viewer (NEOW)
CMSC495 Capstone project

# Overview

NEOW is a graphical user interface (GUI) based program. Its purpose is to help the user to identify near earth objects (NEOs) that are very close to earth. It fetches data from the National Aeronautics and Space Administration (NASA) Jet Propulsion Laboratory (JPL) website via their API. It formats the data to make it user friendly before displaying it on the GUI. A user then has the ability to search and filter a specific NEO or an asteroid by name.

# Code Documentation 

We used the Sphinx tool to generate documentation from docstrings for our code. To view the documentation HTML page, navigate to the following website via a browser:

`capstone-main\docs\_build\html\index.html`

# Usage 

## (Tested using PyCharm IDE with Python 3.8 on Windows)

Run the frontend.py file in your Python interpreter or IDE.

For example:

In PyCharm open `frontend.py`, then press `SHIFT` + `F10`

You can search for an asteroid via clicking on an asteroid or searching by name. Searching an empty search bar will refresh the list.

Note: there is a known Python bug for MacOS with tkinter, you need Python 3.11 to make it work. The GUI will not work on Python 3.9

# Unit Testing

In the `capstone-main` root folder you can run (In Pycharm running on Windows) `pytest.exe -v -W ignore::DeprecationWarning` You should get 10 tests with status PASSED. If you are using Linux/MacOS the pytest.exe binary might be named differently.
