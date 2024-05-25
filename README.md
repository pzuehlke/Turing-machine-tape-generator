# Turing Machine Tape Generator

This repository contains Python scripts designed to automate the generation and compilation of [LaTeX](https://en.wikipedia.org/wiki/LaTeX)/[TikZ](https://en.wikipedia.org/wiki/PGF/TikZ) source code for visually representing the tape of a [Turing machine](https://en.wikipedia.org/wiki/Turing_machine).


![Examples](examples.png)


The generated diagram follows the same style as that in Charles Petzold's book [_The Annotated Turing_](https://www.charlespetzold.com/books/). It consists of a grid of squares containing characters from a given input string, with an ultra-thick border around a specified square to indicate the current position of the head, a customizable total number of squares and a few style options.

## Structure

The program consists of three scripts:

1. `generate_tikz_code.py` - Generates the LaTeX/TikZ source code and saves it to the file `tikz_code.tex`.
2. `compile_latex.py` - Compiles the generated LaTeX file to a PDF and saves it inside an `output` folder together with associated `.aux` and `.log` files.
3. `main.py` - Main script; calls the other two scripts to produce the LaTeX source code and PDF files.

## Requirements

* Python 3.x
* A LaTeX distribution with `pdflatex` (e.g., TeX Live, MiKTeX)
* The [TikZ](https://en.wikipedia.org/wiki/PGF/TikZ) package for LaTeX

## Usage

Just edit the variables in `main.py` to customize the tape's content according to the explanations there. Here's the code used to produce the first example in the preceding figure:
```python
s = "r e c u r s i o n !"  # The string to be printed on the tape
head = 15    # The position of the head (0-based)
length = 20  # The total number of squares
style = "c"  # Additional style options
```

Then run the main script through the Python interpreter:
```bash
python3 main.py
```