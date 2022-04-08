from collections import defaultdict
from promise import Promise
from promise.dataloader import DataLoader

from .models import Book, Review


class ReviewByBookIdLoader(DataLoader):
    def batch_load_fn(self, book_ids):
        reviews_by_book_ids = defaultdict(list)

        for review in Review.objects.filter(book_id__in=book_ids).iterator():
            reviews_by_book_ids[review.book_id].append(review)
        return Promise.resolve([reviews_by_book_ids.get(book_id, [])
                                for book_id in book_ids])
