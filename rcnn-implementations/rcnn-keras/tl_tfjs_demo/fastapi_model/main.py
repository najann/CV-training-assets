import re

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

# configure CORSMiddleware so that the
# frontend can request the model files
origins = [
    # "http://0.0.0.0:8080/",
    # "http://0.0.0.0:8080",
    # "http://localhost:8080/",
    # "http://localhost:8080",
    # "http://127.0.0.1:8080/",
    # "http://127.0.0.1:8080",
    # "https://0.0.0.0:8080/",
    # "https://0.0.0.0:8080",
    # "https://localhost:8080",
    # "https://localhost:8080/",
    # "https://127.0.0.1:8080",
    # "https://127.0.0.1:8080/",
    # "http://api/",
    # "https://api/",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oneMonth = "max-age=2592000"

# initial request
@app.get("/")
async def root(response: Response):
    response.headers["Cache-Control"] = oneMonth
    return FileResponse('model-tfjs-layer/model.json')

# subsequent (automatic) requests
@app.get("/{shard}")
async def sub_req(shard, response: Response):
    response.headers["Cache-Control"] = oneMonth
    regex = r'^group1-shard(\d{1,2})of(\d{1,2}\.)bin$'
    if re.match(regex, shard):
        return FileResponse(f'model-tfjs-layer/{shard}')
