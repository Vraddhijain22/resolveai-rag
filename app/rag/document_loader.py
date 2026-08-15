# Purpose: Read PDF files and extract their text page-by-page.
# This is the FIRST step of our RAG pipeline:
from pathlib import Path
from pypdf import PdfReader


def load_pdf(file_path: str) -> list[dict]:
    """
    Extract text from every page of a PDF.
    """
# STEP 1: Open the PDF
    reader = PdfReader(file_path)
# STEP 2: Create an empty list
    documents = []
# STEP 3: Go through every page
    for page_number, page in enumerate(reader.pages, start=1):
# STEP 4: Extract text from the current page
        text = page.extract_text()
# STEP 5: Check whether the page actually contains text
        if text and text.strip():
# STEP 6: Store the extracted information
            documents.append({
                "text": text.strip(),
                "page": page_number,
                "source": Path(file_path).name
            })
# STEP 7: Return all extracted pages
    return documents