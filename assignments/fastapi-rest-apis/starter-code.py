"""Starter code for the FastAPI REST API assignment."""

from fastapi import FastAPI

app = FastAPI(title="Books API")


@app.get("/")
def read_root():
    """Confirm that the API is running."""
    return {"message": "Books API is running"}


# Add your Book and BookCreate models here.
# Add the GET /books, GET /books/{book_id}, and POST /books routes here.


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)