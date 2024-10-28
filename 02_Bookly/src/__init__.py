from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    title="Bookly", 
    description="This is a Books API", 
    version=version
)

app.include_router(book_router, prefix=f"/api/{version}/book", tags=["books"])