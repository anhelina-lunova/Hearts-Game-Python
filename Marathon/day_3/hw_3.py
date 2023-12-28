from typing import List


class Author:
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


class Genre:
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
    :param description: Опис книги.
    :param language: Мова книги.
    :param authors: Список авторів книги.
    :param genres: Список жанрів книги.
    :param year_of_publication: Рік публикації книги.
    :param isbn: ISBN книги.
    """

    def __init__(
        self,
        title: str,
        description: str,
        language: str,
        authors: List[Author],
        genres: List[Genre],
        year_of_publication: int,
        isbn: str,
    ):
        self.title = title
        self.description = description
        self.language = language
        self.authors = authors
        self.genres = genres
        self.year_of_publication = year_of_publication
        self.isbn = isbn

    def __str__(self):
        return (
            f"({self.language}) Book '{self.title}' - {self.description}. "
            f"Written by {self.authors} in {self.year_of_publication}"
        )

    def __repr__(self):
        return (
            f"Book({self.title}, {self.description}, {self.language}, {self.authors}, {self.genres}, "
            f"{self.year_of_publication}, {self.isbn})"
        )

    def __eq__(self, other: "Book") -> bool:
        return self.title == other.title and self.authors == other.authors


def main():
    george_orwell = Author("George", "Orwell", 1903)

    distopia = Genre(
        "Distopia",
        "is a speculated community or society that is extremely bad or frightening",
    )

    political_satire = Genre(
        "Political satire",
        "is a type of satire that specializes in gaining entertainment from politics",
    )

    nineteen_eighty_four = Book(
        "1984",
        "is a dystopian novel and cautionary tale",
        "en",
        [george_orwell],
        [distopia],
        1949,
        "9780241453513",
    )

    animal_farm = Book(
        "Animal Farm",
        "is a beast fable, in the form of a satirical allegorical novella",
        "en",
        [george_orwell],
        [political_satire],
        1945,
        "9781847498588",
    )

    print(nineteen_eighty_four)
    print(animal_farm)


if __name__ == "__main__":
    main()
