import os
from sentence_transformers import SentenceTransformer, util

# Path to save/load the model
MODEL_DIR = "./local_model"

# Load or download model
if not os.path.exists(MODEL_DIR):
    print("Model not found locally. Downloading...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    model.save(MODEL_DIR)
else:
    model = SentenceTransformer(MODEL_DIR)

def get_content_similarity(ref_text: str, student_text: str) -> float:
    embedding_ref = model.encode(ref_text, convert_to_tensor=True)
    embedding_student = model.encode(student_text, convert_to_tensor=True)
    similarity_score = util.cos_sim(embedding_ref, embedding_student).item()
    return similarity_score


