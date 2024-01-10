def generate_tikz_tape(s: str, index: int, length: int, style: str) -> str:
    """
    Generates LaTeX source code for a TikZ diagram representing the tape
    of a Turing machine with specified characteristics, in the style of
    Petzold's "The Annotated Turing".
    Parameters:
        * s: The input string to be displayed inside the tape's squares.
        * index: The index of the square to be highlighted with an ultra-thick
          border, representing the current position of the machine's head.
        * length: The number of squares (excluding extra squares) in the tape.
        * style: A string specifying some options for the tape. The presence of
          the characters 'c', 'l' or 'r' has the following effects:
            - 'c': Center the TikZ picture on the screen.
            - 'l': Add two extra squares at the beginning, with left edges
              missing and "..." displayed.
            - 'r': Add two extra squares at the end, with right edges
              missing and "..." displayed.
    Output: The LaTeX source code for generating the TikZ diagram.
    Writes: The LaTeX code to a file named "tikz_code.txt".
    """
    if len(s) > length:
        raise ValueError("The length of the string cannot exceed the number"
                         "of squares!")
    if index >= length:
        raise ValueError("The given index exceeds the number of squares!")

    # Begin the environments:
    tikz_code = "\\begin{tikzpicture}\n"
    if 'c' in style:    # The picture should be centered.
        tikz_code = "\\begin{center}\n" + tikz_code

    # Add extra squares at the left and right ends if necessary:
    left_extra = 2 if 'l' in style else 0
    right_extra = 2 if 'r' in style else 0
    total_length = length + left_extra + right_extra

    # Define the coordinate points:
    for i in range(total_length + 1):
        tikz_code += f"\\coordinate (A{i}) at ({0.5 * i}, 0, 0);\n"
        tikz_code += f"\\coordinate (B{i}) at ({0.5 * i}, 0.5, 0);\n"

    # Add the string's characters to the diagram:
    for i, c in enumerate(s):
        tikz_code += (f"\\coordinate (C{i + left_extra}) at"
                      f"({0.5 * (i + left_extra) + 0.25}, 0.25, 0);\n")
        tikz_code += f"\\node at (C{i + left_extra}) {{{c}}};\n"

    # Add "..." to the specified squares if asked to:
    if 'l' in style:
        tikz_code += "\\coordinate (D) at (0.5, 0.25, 0);\n"
        tikz_code += "\\node at (D) {$ \\cdots $};\n"
    if 'r' in style:
        tikz_code += ("\\coordinate (E) at"
                      f"({0.5 * (total_length - 2)}, 0.25, 0);\n")
        tikz_code += "\\node at (E) {$ \\cdots $};\n"

    # Draw the vertical edges:
    for i in range(left_extra, length + left_extra):
        tikz_code += f"\\draw (B{i}) -- (A{i});\n"
    if 'l' not in style:
        tikz_code += "\\draw (B0) -- (A0);\n"

    # Draw the bottom and top edges:
    b = 1 if 'l' in style else 0
    e = total_length - 2 if 'r' in style else total_length - 1
    tikz_code += f"\\draw (A{b}) -- (A{e});\n"
    tikz_code += f"\\draw (B{b}) -- (B{e});\n"

    # Draw an ultra-thick square grid around the specified index:
    tikz_code += (f"\\draw[ultra thick] (B{index + left_extra}) --"
                  f"(A{index + left_extra})"
                  f"-- (A{index + left_extra + 1}) --"
                  f"(B{index + left_extra + 1}) -- cycle;\n")

    # Close the environments:
    tikz_code += "\\end{tikzpicture}\n"
    if 'c' in style:
        tikz_code += "\\end{center}\n"
    tikz_code += "\\medskip"

    # Write the output to a file:
    with open("tikz_code.txt", "w") as outfile:
        outfile.write(tikz_code)
    print("The TikZ code has been successfully generated!")

    return tikz_code


# Example 1:
s = "r e c u r s i o n !"
index = 15
length = 20
style = "c"
tikz_code = generate_tikz_tape(s, index, length, style)

# Example 2:
s = "@1 1 0 1 0 1 1x0 1"
index = 14
length = 20
style = "lrc"
tikz_code = generate_tikz_tape(s, index, length, style)

# Example 3:
s = "@0 1x0 0 1x0 1x0 1x"
index = 7
length = 20
style = "rc"
tikz_code = generate_tikz_tape(s, index, length, style)

# Example 4:
s = "3:j0[Y!ZaLh?8/btm27"
index = 1
length = 20
style = "lc"
tikz_code = generate_tikz_tape(s, index, length, style)
