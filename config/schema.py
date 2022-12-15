import strawberry
import typing


@strawberry.type
class Movie:
    pk: int
    title: str
    year: int
    rating: int


movies_db = [
    Movie(pk=1, title="Godfather", year=1990, rating=0),
]


@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> typing.List[Movie]:
        return movies_db

    @strawberry.field
    def movie(self, movie_pk: int) -> Movie:
        return movies_db[movie_pk - 1]

    @strawberry.field
    def ping(self) -> str:
        return "pong"


schema = strawberry.Schema(query=Query)
