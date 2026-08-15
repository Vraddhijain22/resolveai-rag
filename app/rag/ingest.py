from pathlib import Path

from app.rag.document_loader import load_pdf
from app.rag.chunker import chunk_text


DOCUMENTS_FOLDER = Path("data/documents")

pdf_files = list(DOCUMENTS_FOLDER.glob("*.pdf"))

all_chunks = []

for pdf_file in pdf_files:

    print("\n" + "=" * 70)
    print(f"Processing: {pdf_file.name}")

    pages = load_pdf(str(pdf_file))

    print(f"Pages extracted: {len(pages)}")

    for page in pages:

        chunks = chunk_text(page["text"])

        for chunk in chunks:

            all_chunks.append({
                "text": chunk,
                "source": page["source"],
                "page": page["page"]
            })

            print(
                f"Created chunk | "
                f"Source: {page['source']} | "
                f"Page: {page['page']}"
            )


print("\n" + "=" * 70)

print(f"Total PDFs: {len(pdf_files)}")
print(f"Total chunks: {len(all_chunks)}")


for index, chunk in enumerate(all_chunks[:5], start=1):

    print("\n" + "-" * 70)
    print(f"Chunk {index}")
    print(f"Source: {chunk['source']}")
    print(f"Page: {chunk['page']}")
    print(f"Text: {chunk['text'][:300]}")