import imp
from django.shortcuts import render

# Create your views here.
from django.utils.functional import cached_property
from graphene_django.views import GraphQLView
from .loaders import ReviewByBookIdLoader


class GQLContext:
    def __init__(self, request):
        self.request = request

    @cached_property
    def user(self):
        return self.request.user

    @cached_property
    def reviews_by_book_id_loader(self):
        return ReviewByBookIdLoader()


class CustomGraphQLView(GraphQLView):
    def get_context(self, request):
        return GQLContext(request)
