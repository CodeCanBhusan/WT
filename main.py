
import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from grammar_checker import grammar_score
from semantic_checker import content_score
from form_checker import form_score
from vocab_check import vocab_score


app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      
    allow_credentials=True,
    allow_methods=["*"],     
    allow_headers=["*"],    
)

class Item(BaseModel):
    ref: str
    ans: str

@app.get("/")
def read_root():
    return "Running...."


@app.post("/swt/")
async def read_item(item: Item):
    try:
        ref_text = item.ref
        ans_text = item.ans

        content_ans= content_score(ref_text, ans_text)
        form_ans = form_score(ans_text)
        grammar_ans = grammar_score(ans_text)
        vocab_ans = vocab_score(ans_text)

        return {
            "content_score": content_ans,
            "form_score": form_ans,
            "grammar_score": grammar_ans,
            "vocab_score": vocab_ans
        }  
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000)) 
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)