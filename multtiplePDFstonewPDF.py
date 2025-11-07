AIM:
To write a python program to combine select pages from many PDFs.
ALGORITHM:
1. Start
2. Import the required module: PyPDF2
3. Create a PdfWriter object to write the final output PDF
4. For each input PDF:
a) Open the file in binary read mode
b) Create a PdfReader object
c) For each required page number:
i) Check if the page exists
ii) Add the selected page to the PdfWriter object
5. Write the combined pages into a new PDF file
6. Close all file streams
7. End
REQUIRED LIBRARY:
1. Page numbers are zero-indexed (0 = page 1).
2. Make sure all input PDF files exist in the same directory or give full paths.
3. Install PyPDF2 if not already installed:
Install using the statement - pip install PyPDF2
PROGRAM:
import PyPDF2
def combine_selected_pages(pdf_info_list, output_filename):
"""
Combines selected pages from multiple PDF files.
:param pdf_info_list: List of tuples (pdf_filename, list_of_page_numbers)
:param output_filename: Name of the output PDF file
"""
pdf_writer = PyPDF2.PdfWriter()
for pdf_file, page_numbers in pdf_info_list:
with open(pdf_file, 'rb') as file:
pdf_reader = PyPDF2.PdfReader(file)
total_pages = len(pdf_reader.pages)
for page_num in page_numbers:
if 0 <= page_num < total_pages:
pdf_writer.add_page(pdf_reader.pages[page_num])
else:
print(f"Page number {page_num} is out of range in {pdf_file}")
with open(output_filename, 'wb') as output_file:
pdf_writer.write(output_file)
print(f"Combined PDF saved as '{output_filename}'")
OUTPUT:
Combined PDF saved as 'combined_output.pdf'
