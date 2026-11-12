from rag.ingestion.loader import get_content
from rag.ingestion.cleaner import clean_content
from rag.ingestion.chunker import get_chunks
raw=get_content()
cleaned=clean_content(raw)
chunks=get_chunks(cleaned)
print(cleaned)
print(len(chunks))
print(chunks[0])
