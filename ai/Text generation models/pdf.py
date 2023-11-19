import PyPDF2
import os

def extract_text_from_pdf(pdf_filename):
    with open(pdf_filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        return text

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Assuming the PDF file name is 'sample.pdf' in the same folder
pdf_file_path = os.path.join(current_directory, 'resume.pdf')

# Extract text from the PDF file
pdf_text = extract_text_from_pdf(pdf_file_path)

# Print the extracted text
print(pdf_text)
