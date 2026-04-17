from fastapi import FastAPI

from .routers.books import router as books_router
from .models import init_db, drop_db
from seed import seed_books

drop_db()
init_db()
seed_books()

app = FastAPI()
app.include_router(books_router)


