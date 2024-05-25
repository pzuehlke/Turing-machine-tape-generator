from generate_tikz_code import generate_tikz_tape
from compile_latex import compile_latex_to_pdf

# Example usage:
if __name__ == "__main__":
    # Edit these variables to generate your own Turing machine tape:
    s = "r e c u r s i o n !"  # The string to be printed on the tape
    head = 15    # The position of the head (0-based)
    length = 20  # The total number of squares
    style = "c"  # Additional style options

    # Here `style` is a string specifying some options for the tape.
    # The presence of the characters 'c', 'l' or 'r' has the following effects:
    #   - 'c': Center the TikZ picture on the screen.
    #   - 'l': Add two extra squares at the beginning, with left edges
    #      missing and "..." displayed.
    #   - 'r': Add two extra squares at the end, with right edges
    #      missing and "..." displayed.

    # Generate TikZ code and save to .tex file:
    generate_tikz_tape(s, head, length, style)

    # Compile the LaTeX file to a PDF:
    latex_file = "tikz_code.tex"
    compile_latex_to_pdf(latex_file, output_dir="output")
