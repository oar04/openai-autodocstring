# Docstring Generator

AutoDocstring is a Python script that generates docstrings for Python functions. At its current state, the script generates a brief sentence that describes the function. However, it will eventually be updated to use the numpydoc format, which is a standard convention for documenting Python code.

## Requirements

* Python 3.6 or higher
* OpenAI API key
* `openai` package
* `ast` package

To install the required packages, run:
* pip install openai
* pip install ast

## Usage

To use the script, simply run the following command in your terminal: python autodocstring.py

This will prompt you to enter the absolute path of the Python file that you want to generate docstrings for. Once you enter the path, the script will add docstrings to the functions in the file.

Please note that the current version of the script only generates basic docstrings and does not follow the numpydoc format. However, we are working on implementing this feature in future updates.
