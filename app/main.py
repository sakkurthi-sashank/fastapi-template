from fastapi import FastAPI
import uvicorn
from config import env


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Server is running"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host=env.settings.host, port=env.settings.port, log_level="info"
    )
