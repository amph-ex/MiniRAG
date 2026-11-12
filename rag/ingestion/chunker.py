def get_chunks(content):
    chunks=[]
    for piece in content.split(". "):
        piece=piece.strip()
        if piece:
            chunks.append(piece)
    return chunks
