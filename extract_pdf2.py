import PyPDF2

pdf_path = r'd:\cv\kreshive_resume.pdf'
try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        print(text)
except Exception as e:
    print(f"Error: {e}")
