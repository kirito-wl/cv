import subprocess

# function to convert the markdown file to pdf
def convert_md_to_pdf(input_file, output_file):
    # command to run pandoc
    command = ['pandoc', input_file, '-o', output_file, '--pdf-engine=pdflatex']

    # run the command
    subprocess.run(command)

# test the function
if __name__ == '__main__':
    input_file = 'Will-CV.md' # markdown file to convert
    output_file = 'Will-CV.pdf' # pdf file to output
    convert_md_to_pdf(input_file, output_file)