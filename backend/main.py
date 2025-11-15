from fastapi import FastAPI

app = FastAPI(title="Token Tase Backend")

@app.get("/health")
def health():
    return {"status": "ok"}
