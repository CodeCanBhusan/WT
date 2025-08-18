def form_score(paragraph):
    """
    Computes form score (0-1) for a paragraph based on:
    - Word count: must be between 5 and 75
    - Must be a single sentence (only one full stop)
    
    Returns:
        dict: {"score": 0 or 1, "remark": "..."}
    """
    # Count words
    word_count = len(paragraph.split())
    # Count full stops
    sentence_count = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')
    
    # Check conditions
    if word_count < 5 or word_count > 75:
        return {"score": 0, "remark": "Word count not in 5-75 range"}
    elif sentence_count != 1:
        return {"score": 0, "remark": "There should be a single sentence"}
    else:
        return {"score": 1, "remark": "Very good!"}

