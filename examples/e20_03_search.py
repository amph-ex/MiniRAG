from rag.ingestion.embedder import get_vector
from rag.ingestion.repository import get_similar_chunks
qeury="Можно ли оплатить заказ полсе получения?"
vector=get_vector(qeury)
chunks=get_similar_chunks(vector,top_k=2)
for text,score in chunks:
    print(f'{score:.3f} | {text}')