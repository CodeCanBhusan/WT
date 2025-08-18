import language_tool_python

# Initialize grammar tool
tool = language_tool_python.LanguageTool('en-US')

def grammar_score(text: str):
    matches = tool.check(text)
    num_errors = len(matches)

    if num_errors == 0:
        return {
            "score": 2,
            "remark": "Has correct grammatical structure",
            "mistakes": []
        }
    
    words = text.split()
    num_words = len(words) if words else 1

    # Error ratio per 5 words
    errors_per_5_words = (num_errors / num_words) * 5

    if errors_per_5_words <= 3:  
        score = 1
        remark = "Contains grammatical errors but with no hindrance to communication"
    else:
        score = 0
        remark = "Has defective grammatical structure which could hinder communication"

    return {
        "score": score,
        "remark": remark,
        "mistakes": matches,
    }
