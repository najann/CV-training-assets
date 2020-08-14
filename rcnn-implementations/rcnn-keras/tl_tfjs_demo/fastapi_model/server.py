from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import re
from fastapi.responses import FileResponse

app = FastAPI()

# configure CORSMiddleware so that the
# frontend can request the model files
origins = [
    "http://127.0.0.1:8081/",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# initial request
@app.get("/")
async def root():
    return FileResponse('model-tfjs-layer/model.json')

# subsequent (automatic) requests
@app.get("/{shard}")
async def sub_req(shard):
    regex = r'^group1-shard(\d{1,2})of(\d{1,2}\.)bin$'
    if re.match(regex, shard):
        return FileResponse(f'model-tfjs-layer/{shard}')
