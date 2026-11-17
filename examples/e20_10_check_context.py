import os
from rag.ingestion.embedder import get_vector
from rag.ingestion.repository import get_similar_chunks
from llm.prompt_builder import build_prompt
from llm.llm import get_ai_response

query = "Сколько стоит доставка?"
chunks = get_similar_chunks(get_vector(query), top_k=4)

print("Фактический промпт:")
print(build_prompt(query, chunks))

mode = os.getenv("RAG_MODE", "demo").strip().lower()
print("Режим:", mode)
print("Ответ:")
print(get_ai_response(query, chunks, mode=mode))