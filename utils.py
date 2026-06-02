from pypdf import PdfReader
import re

def extract_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    # Remove extra blank lines
    text = re.sub(r'\n\s*\n+', '\n\n', text)

    # Remove lines that contain only numbers
    text = re.sub(r'^\d+\s*$', '', text, flags=re.MULTILINE)

    # Remove lines like:
    # 1.
    # 2.
    text = re.sub(r'^\d+\.\s*$', '', text, flags=re.MULTILINE)

    return text.strip()