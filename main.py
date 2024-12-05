from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="web", html=True), name="web")

if __name__ == "main":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

