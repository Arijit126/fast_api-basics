@app.get("/")
def read_root():
    return {"message":"Hello API!"}

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.get("/books")
def get_books():
    return books

@app.get("/authors")
def get_authors():
    for book in books:
        if book["Author"] not in authors:
            authors.append(book["Author"])
    return authors

@app.get("/books/{book_id}")
def get_book_byID(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error":"book not found"}

@app.get("/authors/{authors_name}")
def get_authors_byName(authors_name:str):
    # for book in books:
    #     if book["Author"] == authors_name:
    #         return authors_name
    # return {"error":"author not found"}
    matches = [book for book in books if book["Author"]==authors_name]
    return matches
