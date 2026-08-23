from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from app.llm.prompts import SYSTEM_PROMPT
from app.config import LLM_MODEL


llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{question}")
])


chain = prompt | llm


context = """
AVAILABLE KNOWLEDGE:

Document: vpn_troubleshooting_runbook.pdf
Page: 1

The VPN may fail after a corporate password change.
Employees should sign out of the VPN client, close it,
restart the application, and authenticate again using
the new password.

END OF AVAILABLE KNOWLEDGE.
"""


question = "What is Nexora's maternity leave policy?"


print("\nQUESTION SENT TO LLM:")
print(question)

print("\nCONTEXT SENT TO LLM:")
print(context)


response = chain.invoke({
    "context": context,
    "question": question
})


print("\nLLM RESPONSE:")
print(response.content)