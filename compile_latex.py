import subprocess
import os

def compile_latex_to_pdf(latex_file: str, output_dir: str = ".") -> None:
    """
    Compiles a LaTeX file to a PDF using pdflatex.

    Parameters:
        * latex_file: The name of the LaTeX file to be compiled.
        * output_dir: The directory where the PDF file will be saved. Default is the current directory.

    Output: None
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Construct the command to compile the LaTeX file to PDF
    command = ["pdflatex", "-output-directory", output_dir, latex_file]

    # Run the command
    try:
        subprocess.run(command, check=True)
        print(f"The PDF has been successfully generated and saved to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error during LaTeX compilation: {e}")

# Example usage
if __name__ == "__main__":
    latex_file = "tikz_code.tex"
    compile_latex_to_pdf(latex_file, output_dir="output")
