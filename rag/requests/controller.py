from rag.ingestion.embedder import get_vector
from rag.ingestion.repository import get_similar_chunks
from llm.llm import get_ai_response

def get(request, top_k=2, mode="demo"):
    request = request.strip()
    if not request:
        raise ValueError("Введите непустой вопрос")
    vector = get_vector(request)
    chunks = get_similar_chunks(vector, top_k=top_k)
    return get_ai_response(request, chunks, mode=mode)
