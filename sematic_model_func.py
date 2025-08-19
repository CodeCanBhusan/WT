
import os
from sentence_transformers import SentenceTransformer, util

MODEL_DIR = "./local_model"
_cached_model = None

def get_model():
    global _cached_model
    if _cached_model is None:
        if not os.path.exists(MODEL_DIR):
            print("Model not found locally. Downloading and caching...")
            _cached_model = SentenceTransformer('all-MiniLM-L6-v2')
            _cached_model.save(MODEL_DIR)
        else:
            _cached_model = SentenceTransformer(MODEL_DIR)
    return _cached_model

def get_content_similarity(ref_text: str, student_text: str) -> float:
    model = get_model()
    embedding_ref = model.encode(ref_text, convert_to_tensor=True)
    embedding_student = model.encode(student_text, convert_to_tensor=True)
    similarity_score = util.cos_sim(embedding_ref, embedding_student).item()
    return similarity_score


