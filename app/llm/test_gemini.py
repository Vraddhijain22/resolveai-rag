from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import (
    GEMINI_API_KEY,
    GEMINI_LLM_MODEL,
)


llm = ChatGoogleGenerativeAI(
    model=GEMINI_LLM_MODEL,
    google_api_key=GEMINI_API_KEY,
)


question = "Explain what RAG is in one simple sentence."

response = llm.invoke(question)


print("\n" + "=" * 70)
print("GEMINI TEST")
print("=" * 70)

print("\nQuestion:")
print(question)

print("\nGemini response:")

if isinstance(response.content, list):

    for item in response.content:

        if isinstance(item, dict) and item.get("type") == "text":

            print(item.get("text", ""))

else:

    print(response.content)