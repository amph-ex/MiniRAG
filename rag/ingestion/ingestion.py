from rag.ingestion.loader import get_content
from rag.ingestion.cleaner import clean_content
from rag.ingestion.chunker import get_chunks
from rag.ingestion.embedder import get_vectors
from rag.ingestion.repository import save
def main():
    content=get_content()
    cleaned=clean_content(content)
    chunks=get_chunks(cleaned)
    if not chunks:
        raise ValueError(f'Нет текста для индексирования')
    vectors=get_vectors(chunks)
    save(vectors)
    print(f'Сохранено фрагментов:{len(vectors)}')
if __name__=="__main__":
    main()

