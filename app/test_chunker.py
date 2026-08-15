from app.rag.chunker import chunk_text


text = """
Nexora Technologies provides employees with several policies.
Employees must follow the password management policy.
Corporate passwords must be at least 12 characters long.
Employees must not reuse corporate passwords on personal websites.
Employees should report suspected password compromise immediately.
Remote employees must use approved devices and secure networks.
Business travel expenses must be submitted within 15 calendar days.
Employees must provide required receipts for reimbursement.
"""


chunks = chunk_text(
    text,
    chunk_size=30,
    overlap=5
)


print(f"Number of chunks: {len(chunks)}")


for index, chunk in enumerate(chunks, start=1):

    print("\n" + "=" * 60)

    print(f"Chunk {index}")

    print(chunk)