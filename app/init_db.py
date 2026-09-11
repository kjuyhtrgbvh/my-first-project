from app.db.db import init_engine
from app.db import crud


def seed():
    init_engine()

    # Очистка, чтобы не дублировать при повторных запусках
    for book in crud.get_books():
        crud.delete_book(book.id)
    for cat in crud.get_categories():
        crud.delete_category(cat.id)

    fiction = crud.create_category("Художественная литература")
    technical = crud.create_category("Техническая литература")

    crud.create_book("Мастер и Маргарита",
                     "Роман Михаила Булгакова", 750.00, fiction.id)
    crud.create_book("Преступление и наказание",
                     "Роман Фёдора Достоевского", 620.50, fiction.id)
    crud.create_book("1984",
                     "Антиутопия Джорджа Оруэлла", 540.00, fiction.id)

    crud.create_book("Python. К вершинам мастерства",
                     "Лучано Рамальо", 1290.00, technical.id)
    crud.create_book("Изучаем SQL",
                     "Алан Бьюли", 980.00, technical.id)
    crud.create_book("Чистый код",
                     "Роберт Мартин", 1100.00, technical.id)

    print("База данных успешно заполнена.")


if __name__ == "__main__":
    seed()