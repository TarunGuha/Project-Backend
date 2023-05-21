from typing import Union, Dict
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query, Request, status
from pydantic import BaseModel
from pydantic import BaseModel, validator
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from caption_service.caption import initialize_caption
from caption_service import caption
from caption_service.helpers import download_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class image_data(BaseModel):
    image_url: Union[str, None] = None


@app.on_event("startup")
def startup():
    # download_model()
    initialize_caption()


@app.get("/")
def read_item():
    return "Hello World"


@app.post("/get_caption")
def get_caption(image_data: image_data):
    return caption.caption.caption_generator(image_data)
