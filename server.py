from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="NIKO Cloud Brain")

class Message(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "NIKO Cloud Running 🚀"}

@app.get("/status")
def status():
    return {"status": "online"}

@app.post("/ask")
def ask(msg: Message):
    return {"response": f"NIKO received: {msg.text}"}
