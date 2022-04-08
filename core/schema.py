import graphene
from graphene_django import DjangoObjectType

from books.models import Book, Review
from graphene_django.debug import DjangoDebug


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = ('id', 'book', 'text')


class BookType(DjangoObjectType):
    reviews = graphene.List(ReviewType)

    class Meta:
        model = Book
        fields = ("id", "title", "desc")

    def resolve_reviews(self, info):
        return info.context.reviews_by_book_id_loader.load(self.id)


class Query(graphene.ObjectType):
    book_with_review = graphene.List(BookType)
    debug = graphene.Field(DjangoDebug, name='_debug')

    def resolve_book_with_review(root, info):
        return Book.objects.all()


schema = graphene.Schema(query=Query)
