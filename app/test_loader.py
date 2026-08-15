# Purpose:Test whether our PDF document_loader.py is working correctly.

from app.rag.document_loader import load_pdf

# STEP 1: Specify the PDF we want to test
file_path = "data/documents/vpn_troubleshooting_runbook.pdf"

# STEP 2: Load the PDF
pages = load_pdf(file_path)

# STEP 3: Print how many pages were loaded
print(f"Number of pages loaded: {len(pages)}")

# STEP 4: Display each page
for page in pages:

    print("\n" + "=" * 70)

    print(f"Source: {page['source']}") # filename
    print(f"Page: {page['page']}")  # page number

# Print the first 1000 characters of the page.
    print(f"Text:\n{page['text'][:1000]}") 