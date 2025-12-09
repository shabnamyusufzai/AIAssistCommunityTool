import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embedAndFaiss(document):
    embedded = model.encode(document)
    embedded = np.array(embedded).astype('float32')
    faissIndex = faiss.IndexFlatL2(embedded.shape[1])
    for emb in embedded:
        faissIndex.add(np.array([emb], dtype='float32'))
    return faissIndex
