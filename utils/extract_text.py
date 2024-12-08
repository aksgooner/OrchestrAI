from PyPDF2 import PdfReader

def extract_text_with_pypdf2(file_path: str) -> str:
    """
    Extracts all text from a PDF file using PyPDF2.
    
    Parameters:
        file_path (str): Path to the PDF file.
    
    Returns:
        str: The extracted text content of the PDF.
    """
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        if page.extract_text():  # Ensure the page has text content
            text += page.extract_text()
    return text