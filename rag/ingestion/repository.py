from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
BASE=Path(__file__).resolve().parents[2]
def get_database_path():
    path= BASE/"database"/"database.txt"
    return path
def save(vectors):
    path=get_database_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w",encoding="utf-8") as database:
        for vector,text in vectors:
            vector_str = " ".join(map(str,vector))
            database.write(f'{vector_str};{text}\n')
def get_similar_chunks(vector,top_k=2):
    if top_k<=0:
        raise ValueError("top_k должен быть больше 0!")
    chunks=[]
    path=get_database_path()
    with path.open("r",encoding="utf-8") as database:
        for line in database:
            if not line.strip():
                continue
            raw_vector,text=line.rstrip("\n").split(";",1)
            numbers=[float(value) for value in raw_vector.split()]
            chunk_vector=np.array(numbers,dtype=float)
            if chunk_vector.shape !=vector.shape:
                raise ValueError(f'Размерности векторов не совпадают')
            score=cosine_similarity([vector],[chunk_vector])[0] [0]
            chunks.append((text.strip(),float(score)))
    if not chunks:
        raise ValueError(f'База пуста.Повторите индексирование')
    chunks.sort(key=lambda item: item[1],reverse=True)
    return chunks[:top_k]

