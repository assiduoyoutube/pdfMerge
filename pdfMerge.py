import os
from PyPDF2 import PdfMerger

def merge_pdfs():
    # Get the current working directory
    current_directory = os.getcwd()

    # Initialize a PDF merger
    pdf_merger = PdfMerger()

    # Get a list of all files in the current directory
    files = [file for file in os.listdir(current_directory) if file.lower().endswith('.pdf')]

    # Merge each PDF file into the merger object
    for file in files:
        pdf_merger.append(os.path.join(current_directory, file))

    # Output merged PDF to a new file
    with open('merged.pdf', 'wb') as merged_pdf:
        pdf_merger.write(merged_pdf)

if __name__ == "__main__":
    merge_pdfs()
