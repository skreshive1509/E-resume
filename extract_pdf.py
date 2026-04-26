import pdfplumber

pdf_path = r'd:\cv\kreshive_resume.pdf'
with pdfplumber.open(pdf_path) as pdf:
    text = '\n'.join([page.extract_text() for page in pdf.pages])
    print(text)