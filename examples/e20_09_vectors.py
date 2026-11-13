from rag.ingestion.chunker import get_chunks
from rag.ingestion.cleaner import clean_content
from rag.ingestion.loader import get_content
from rag.ingestion.embedder import get_vectors
from rag.ingestion.embedder import get_vector
raw=get_content()
raw=clean_content(raw)
chunks=get_chunks(raw)
vector=get_vector("Как оплатить заказ?")
vectors=get_vectors(chunks)
print(vector.shape)
print(len(vectors))
print(vectors[0][1])
print(vectors[0][0].shape)