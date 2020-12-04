from typing import Iterable, Any


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection: Iterable[Any], items_per_page: int):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        collection_len = len(self.collection)
        if collection_len <= self.items_per_page:
            return 1
        elif collection_len % self.items_per_page == 0:
            return int(collection_len / self.items_per_page)
        else:
            return int((float(collection_len) // self.items_per_page)) + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):

        page_range = range(0, self.page_count())
        if page_index not in page_range:
            return - 1
        
        if page_index < page_range[-1]:
            return self.items_per_page
        else:
            return self.item_count() % self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        
        if item_index not in range(0, self.item_count()):
            return -1
        else:
            return item_index // self.items_per_page

    def get_page(self, page_index):

        page_range = range(0, self.page_count())
        if page_index not in page_range:
            return - 1

        if page_index == 0:
            return self.collection[:self.items_per_page]
        else:
            words_to_skip = self.items_per_page * (page_index)

            return self.collection[words_to_skip: (words_to_skip + self.items_per_page)]
        

# collection = range(1,25)
# helper = PaginationHelper(collection, 10)


words = "Hello my name is Nick and I like to do stuff and I really do not think this sentence makes sense okay bye.".split()

paginator = PaginationHelper(words, 4)

print(paginator.item_count())
print(paginator.items_per_page)
print(paginator.page_count())

print(paginator.page_item_count(0))
print(paginator.page_item_count(5))
print(paginator.page_index(22))
print(paginator.get_page(0))
print(paginator.get_page(1))
print(paginator.get_page(2))
print(paginator.get_page(3))
print(paginator.get_page(4))
print(paginator.get_page(5))
print(paginator.get_page(6)) ## out of range, return -1
