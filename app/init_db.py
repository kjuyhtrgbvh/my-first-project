from app.db.db import init_engine, get_session
from app.db import crud


def seed():
    init_engine()

    with get_session() as session:
        # Очистка, чтобы не дублировать при повторных запусках
        for book in crud.get_books(session):
            crud.delete_book(session, book.id)
        for cat in crud.get_categories(session):
            crud.delete_category(session, cat.id)

        fiction = crud.create_category(session, "Художественная литература")
        technical = crud.create_category(session, "Техническая литература")

        crud.create_book(session, "Мастер и Маргарита",
                         "Роман Михаила Булгакова", 750.00, fiction.id)
        crud.create_book(session, "Преступление и наказание",
                         "Роман Фёдора Достоевского", 620.50, fiction.id)
        crud.create_book(session, "1984",
                         "Антиутопия Джорджа Оруэлла", 540.00, fiction.id)

        crud.create_book(session, "Python. К вершинам мастерства",
                         "Лучано Рамальо", 1290.00, technical.id)
        crud.create_book(session, "Изучаем SQL",
                         "Алан Бьюли", 980.00, technical.id)
        crud.create_book(session, "Чистый код",
                         "Роберт Мартин", 1100.00, technical.id)

    print("База данных успешно заполнена.")


if __name__ == "__main__":
    seed()