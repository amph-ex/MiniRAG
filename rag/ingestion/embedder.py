from sentence_transformers import SentenceTransformer
MODEL_NAME="paraphrase-multilingual-MiniLM-L12-v2"
model = SentenceTransformer(MODEL_NAME, device="cpu")
def get_vector(content):
    return model.encode(content, show_progress_bar=False)
def get_vectors(chunks):
    result=[]
    for chunk in chunks:
        vectror = get_vector(chunk)
        result.append([vectror, chunk])
    return result