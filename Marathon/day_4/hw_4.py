# Модифікувати клас книги з ДЗ 3 таким чином, щоб параметри які ми передаємо при ініціалізації екземпляру були:
# - name, language, year - обовʼязковими
# - автори - передавались не списком а як звичайні позиційні аргументи
# - опис книги, isbn, genres - необовʼяккові параметри і лише як ключові
# (підказки тут https://docs.python.org/3/tutorial/controlflow.html#special-parameters)
#
#
# - створіть метод у книги який повертає вік книги в роках (відносно поточного)
# (підказки тут - https://docs.python.org/3/library/datetime.html)

from typing import List, Optional
from datetime import date


class Author:  # без змін
    """
    Клас автора книги.

    :param first_name: Імʼя автора.
    :param last_name: Прізвище автора.
    :param year_of_birth: Рік народження автора.
    """

    def __init__(self, first_name: str, last_name: str, year_of_birth: int):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

    def __str__(self):
        return f"{self.first_name} {self.last_name} was born in ({self.year_of_birth})"

    def __repr__(self):
        return f"Author({self.first_name}, {self.last_name}, {self.year_of_birth})"

    def __eq__(self, other: "Author") -> bool:
        return (
            self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.year_of_birth == other.year_of_birth
        )


class Genre:  # без змін
    """
    Клас жанру книги.

    :param name: Назва жанру.
    :param description: Опис жанру.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Genre({self.name}, {self.description})"

    def __eq__(self, other: "Genre") -> bool:
        return self.name == other.name


class Book:
    """
    Клас книги.

    :param title: Назва книги.
    :param language: Мова книги.
    :param year: Рік публикації книги.
    :param authors: Автори книги (позиційні аргументи).
    :param description: Опис книги (необов'язковий ключовий аргумент).
    :param genres: Жанри книги (необов'язковий ключовий аргумент).
    :param isbn: ISBN книги (необов'язковий ключовий аргумент).
    """

    def __init__(
        self,
        title: str,
        language: str,
        year: int,
        *authors: Author,  # Автори як ключовий аргумент
        description: Optional[str] = None,
        genres: Optional[List[Genre]] = None,
        isbn: Optional[str] = None,
    ):
        self.title = title
        self.language = language
        self.year_of_publication = year
        self.authors = authors
        self.description = description
        self.genres = genres or []
        self.isbn = isbn

    # __str__ та get_age - змінено, інші - без змін

    def __str__(self):
        return (
            f"({self.language}) Book '{self.title}' - {self.description or 'No description'}. "
            f"Written by {self.authors} in {self.year_of_publication}"
        )

    def __repr__(self):
        return (
            f"Book({self.title}, {self.description}, {self.language}, {self.authors}, {self.genres}, "
            f"{self.year_of_publication}, {self.isbn})"
        )

    def __eq__(self, other: "Book") -> bool:
        return self.title == other.title and self.authors == other.authors

    def get_age(self) -> int:
        """Повертає вік книги в роках (відносно поточного року)"""
        current_year = date.today().year
        return current_year - self.year_of_publication


def main():  # без змін
    ...


if __name__ == "__main__":
    main()

# Authors
eric_arthur_blair = Author("George", "Orwell", 1903)
george_orwell = Author("George", "Orwell", 1903)
steve_freeman = Author("Steve", "Freeman", 1958)
nat_pryce = Author("Nat", "Pryce", 1960)

# Genres
distopia = Genre(
    "Distopia",
    "is a speculated community or society that is extremely bad or frightening",
)
political_satire = Genre(
    "Political satire",
    "is a type of satire that specializes in gaining entertainment from politics",
)
computers_and_technology = Genre("Computers & Technology", "")
programming = Genre("Programming", "")

keep_the_aspidistra_flying = Book(
    "Keep the Aspidistra Flying", "en", 1936, eric_arthur_blair
)

# Books
nineteen_eighty_four = Book(
    "1984",
    "en",
    1949,
    george_orwell,  # Автор передається як ключовий аргумент
    description="is a dystopian novel and cautionary tale",
    genres=[distopia],
    isbn="9780241453513",
)

animal_farm = Book(
    "Animal Farm",
    "en",
    1945,
    george_orwell,  # Автор передається як ключовий аргумент
    description="is a beast fable, in the form of a satirical allegorical novella",
    genres=[political_satire],
    isbn="9781847498588",
)

growing_oo_soft = Book(
    "Growing Object-Oriented Software, Guided by Tests",
    "en",
    2009,
    steve_freeman,
    nat_pryce,
    description="If you want to be an expert in the state of the art in TDD, "
    "you need to understand the ideas in this book",
    genres=[computers_and_technology, programming],
    isbn="978-0321503626",
)

growing_oo_soft_without_descr = Book(
    "Growing Object-Oriented Software, Guided by Tests",
    "en",
    2009,
    steve_freeman,
    nat_pryce,
    genres=[computers_and_technology, programming],
    isbn="978-0321503626",
)

growing_oo_soft_without_genres = Book(
    "Growing Object-Oriented Software, Guided by Tests",
    "en",
    2009,
    steve_freeman,
    nat_pryce,
    description="If you want to be an expert in the state of the art in TDD, "
    "you need to understand the ideas in this book",
    isbn="978-0321503626",
)

growing_oo_soft_without_isbn = Book(
    "Growing Object-Oriented Software, Guided by Tests",
    "en",
    2009,
    steve_freeman,
    nat_pryce,
    description="If you want to be an expert in the state of the art in TDD, "
    "you need to understand the ideas in this book",
    genres=[computers_and_technology, programming],
)

growing_oo_soft_without_all = Book(
    "Growing Object-Oriented Software, Guided by Tests",
    "en",
    2009,
    steve_freeman,
    nat_pryce,
)

print(nineteen_eighty_four)
print(animal_farm)
print(growing_oo_soft)
print(growing_oo_soft_without_descr)
print(growing_oo_soft_without_genres)
print(growing_oo_soft_without_isbn)
print(growing_oo_soft_without_all)

print(
    f"Book '{keep_the_aspidistra_flying.title}' by {eric_arthur_blair.first_name} {eric_arthur_blair.last_name} "
    f"was written {keep_the_aspidistra_flying.get_age()} years ago"
)

print(eric_arthur_blair == george_orwell)
