from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from model.model import Model
from pathlib import Path
from pydantic import BaseModel
from starlette.responses import FileResponse

# ------------------------------ Communication models ------------------------------

class ModelIdentificator(BaseModel):
    id: str

class ModelInput(BaseModel):
    inpt: str

# ------------------------------ Initial configuration and variables ------------------------------

# Create a FastAPI application instance
app = FastAPI()

# Mount the 'web' directory as '/static' to serve static files
app.mount('/static', StaticFiles(directory=Path(__file__).parent.parent / 'web'), name='static')

# Creates a Model instance, that is an abstractions to handle different language models
model = Model()

# ------------------------------ Endpoints ------------------------------

@app.get('/')
async def get_index():
    """
    Serves the index.html file for the main application.

    This function handles requests to the root URL (/) of the application.
    It retrieves the index.html file from the 'web' directory within the project structure
    and returns it as a FileResponse object, making it accessible to the browser.
    """

    return FileResponse(Path(__file__).parent.parent / 'web' / 'index.html')

@app.post('/api/select-model')
async def select_model(mi: ModelIdentificator):
    """
    Handles POST requests to the '/api/select-model' endpoint for model selection.

    This function expects a request body containing data in the format of a ModelIdentificator object (likely a custom class).
    It's intended to handle the selection of a specific model based on the provided identifier.
    """

    model.load(mi.id)

    return {}

@app.post('/api/run-ginput')
async def run_ginput(mi: ModelInput):
    """
    Handles POST requests to the '/api/run-ginput' endpoint for running general inputs.

    This function expects a request body containing data in the format of a ModelInput object (likely a custom class).
    It's intended to handle processing of general input data using a model (presumably selected through the '/api/select-model' endpoint).
    """

    output = model.run(mi.inpt)
    
    return {'output': output} 