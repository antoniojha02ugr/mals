from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pydantic import BaseModel
from starlette.responses import FileResponse

import time;

# Define the model for the client's JSON request
class Message(BaseModel):
    message: str

app = FastAPI()

app.mount('/static', StaticFiles(directory=Path(__file__).parent.parent / 'web'), name='static')

# Route to serve the index.html file when the root URL is accessed
@app.get('/')
async def get_index():
    # Return the index.html file as a response
    return FileResponse(Path(__file__).parent.parent / 'web' / 'index.html')

@app.post('/api/select-model')
async def select_model(message: Message):
    print(message.message)

    time.sleep(2)

    return {}