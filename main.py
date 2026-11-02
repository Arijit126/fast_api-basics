from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Book(BaseModel):
    title:str
    author:str

books = [
    {"id":1,"Book":"Taranath Tantrik","Author":"Taradas Bannerjee"},
    {"id":2,"Book":"Chander Pahar","Author":"Bibhutibhusan Bannerjee"},
    {"id":3,"Book":"Sera Bhuter Golpo","Author":"Bibhutibhusan Bannerjee"},
]

authors = []

@app.post("/books")
def create_book(book: Book):
    new_book = {
        "id":len(books)+1,
        "title":book.title,
        "author":book.author
    }
    books.append(new_book)
    return new_book

@app.get("/books")
def get_books():
    return books