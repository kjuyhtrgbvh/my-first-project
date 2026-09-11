from app.db.db import get_session
from app.db.models import Category, Book


# ---------- Category ----------

def create_category(title: str) -> Category:
    session = get_session()
    try:
        obj = Category(title=title)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj
    finally:
        session.close()


def get_category(category_id: int):
    session = get_session()
    try:
        return session.query(Category).filter(Category.id == category_id).first()
    finally:
        session.close()


def get_categories():
    session = get_session()
    try:
        return session.query(Category).all()
    finally:
        session.close()


def update_category(category_id: int, new_title: str):
    session = get_session()
    try:
        obj = session.query(Category).filter(Category.id == category_id).first()
        if obj:
            obj.title = new_title
            session.commit()
            session.refresh(obj)
        return obj
    finally:
        session.close()


def delete_category(category_id: int) -> bool:
    session = get_session()
    try:
        obj = session.query(Category).filter(Category.id == category_id).first()
        if obj:
            session.delete(obj)
            session.commit()
            return True
        return False
    finally:
        session.close()


# ---------- Book ----------

def create_book(title: str, description: str, price: float,
                category_id: int, url: str = "") -> Book:
    session = get_session()
    try:
        obj = Book(
            title=title,
            description=description,
            price=price,
            url=url,
            category_id=category_id,
        )
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj
    finally:
        session.close()


def get_book(book_id: int):
    session = get_session()
    try:
        return session.query(Book).filter(Book.id == book_id).first()
    finally:
        session.close()


def get_books():
    session = get_session()
    try:
        return session.query(Book).all()
    finally:
        session.close()


def get_books_by_category(category_id: int):
    session = get_session()
    try:
        return session.query(Book).filter(Book.category_id == category_id).all()
    finally:
        session.close()


def update_book(book_id: int, **kwargs):
    session = get_session()
    try:
        obj = session.query(Book).filter(Book.id == book_id).first()
        if obj:
            for key, value in kwargs.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            session.commit()
            session.refresh(obj)
        return obj
    finally:
        session.close()


def delete_book(book_id: int) -> bool:
    session = get_session()
    try:
        obj = session.query(Book).filter(Book.id == book_id).first()
        if obj:
            session.delete(obj)
            session.commit()
            return True
        return False
    finally:
        session.close()