

from sematic_model_func import get_content_similarity

def content_score(ref_text, submitted_text):
    """
    Maps a cosine similarity score (0-1) to a 0-4 scale.
    
    Args:
        cosine_similarity (float): Value between 0 and 1.
    
    Returns:
        int: Score between 0 and 4
    """

    similarity=get_content_similarity(ref_text, submitted_text)

    if similarity >= 0.85:
        return {
            "score": 4,
            "remark": "Comprehensive summary; full comprehension; effective paraphrasing and smooth flow."
        }
    elif similarity >= 0.7:
        return {
            "score": 3,
            "remark": "Adequate summary; good comprehension; paraphrasing present; minor omissions; logical flow."
        }
    elif similarity >= 0.5:
        return {
            "score": 2,
            "remark": "Partial summary; basic comprehension; ideas repeated from source; some clarity issues."
        }
    elif similarity >= 0.3:
        return {
            "score": 1,
            "remark": "Relevant but limited; disconnected ideas; main points missing; hard to follow."
        }
    else:
        return {
            "score": 0,
            "remark": "Too limited; no comprehension of source; main ideas omitted or misrepresented."
        }