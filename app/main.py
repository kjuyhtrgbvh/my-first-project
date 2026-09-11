from app.db import crud


def main():
    categories = crud.get_categories()

    print("=" * 60)
    print("КАТАЛОГ КНИГ")
    print("=" * 60)

    for category in categories:
        print(f"\nКатегория: {category.title} (id={category.id})")
        print("-" * 60)
        books = crud.get_books_by_category(category.id)
        if not books:
            print("  (нет книг)")
            continue
        for book in books:
            print(f"  • {book.title}")
            print(f"      Описание: {book.description}")
            print(f"      Цена:     {book.price} руб.")
            print(f"      URL:      {book.url or '—'}")
            print()

    print("=" * 60)
    print(f"Всего категорий: {len(categories)}")
    print(f"Всего книг:      {len(crud.get_books())}")
    print("=" * 60)


if __name__ == "__main__":
    main()