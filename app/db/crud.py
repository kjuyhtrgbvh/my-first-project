from sqlalchemy.orm import Session

from app.db.models import Category, Book


# ---------- Category ----------

def create_category(session: Session, title: str) -> Category:
    obj = Category(title=title)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


def get_category(session: Session, category_id: int):
    return session.query(Category).filter(Category.id == category_id).first()


def get_categories(session: Session):
    return session.query(Category).all()


def update_category(session: Session, category_id: int, new_title: str):
    obj = session.query(Category).filter(Category.id == category_id).first()
    if obj:
        obj.title = new_title
        session.commit()
        session.refresh(obj)
    return obj


def delete_category(session: Session, category_id: int) -> bool:
    obj = session.query(Category).filter(Category.id == category_id).first()
    if obj:
        session.delete(obj)
        session.commit()
        return True
    return False


# ---------- Book ----------

def create_book(session: Session, title: str, description: str, price: float,
                category_id: int, url: str = "") -> Book:
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


def get_book(session: Session, book_id: int):
    return session.query(Book).filter(Book.id == book_id).first()


def get_books(session: Session):
    return session.query(Book).all()


def get_books_by_category(session: Session, category_id: int):
    return session.query(Book).filter(Book.category_id == category_id).all()


def update_book(session: Session, book_id: int, **kwargs):
    obj = session.query(Book).filter(Book.id == book_id).first()
    if obj:
        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        session.commit()
        session.refresh(obj)
    return obj


def delete_book(session: Session, book_id: int) -> bool:
    obj = session.query(Book).filter(Book.id == book_id).first()
    if obj:
        session.delete(obj)
        session.commit()
        return True
    return False