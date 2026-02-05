
from fastapi import FastAPI, UploadFile, File
from typing import List

app = FastAPI(title="PM Copilot v2")

@app.get("/")
def root():
    return {"message": "PM Copilot backend running"}

@app.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    return {"files": [f.filename for f in files]}
