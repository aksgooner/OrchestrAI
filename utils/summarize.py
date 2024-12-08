from utils.extract_text import extract_text_with_pypdf2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import pipeline
import openai

def summarize_pdf(file_path):
    """
        Summarizes the content of a PDF file using PyPDF2 for text extraction
        and Hugging Face's transformers library for summarization.
        
        Parameters:
            file_path (str): Path to the PDF file to summarize.
            chunk_size (int): Maximum size of each text chunk.
            chunk_overlap (int): Overlap between consecutive text chunks.
        
        Returns:
            str: The summarized content of the PDF.
    """
    
    # Step 1: Extract text from the PDF

    raw_text = extract_text_with_pypdf2(file_path)
    
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Free-tier model
        messages=[
            {"role": "system", "content": "You are a helpful assistant for summarizing documents."},
            {"role": "user", "content": f"Summarize this document:\n {raw_text}"},
        ]
    )

    summary = response.choices[0].message.content

    return summary
