from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def index() -> dict:
    return {"message": "Hello World"}


@app.get("/greet")
# Optional query parameter should be at the last or all the query parameter should have a default value
async def greet_name(age: int = 0, name: Optional[str] = "User") -> dict:
    return {"message": f"Hello {name}", "age": age}


# Book Schema
class BookCreateModel(BaseModel):
    title: str
    author: str
    description: str


@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author,
        "description": book_data.description,
    }


@app.get("/get_headers", status_code=201)
async def get_headers(
    accept: str = Header(None),
    connection: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    request_headers = {}

    request_headers["accept"] = accept
    request_headers["connection"] = connection
    request_headers["content_type"] = content_type
    request_headers["user_agent"] = user_agent
    request_headers["host"] = host

    return request_headers
