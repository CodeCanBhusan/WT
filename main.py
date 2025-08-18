
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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


@app.post("/swt/")
async def read_item(item: Item):
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
