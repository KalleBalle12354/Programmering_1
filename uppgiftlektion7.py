"""
class book:
    def __init__(Title, author, pages)
        self.title = title
        self.author = author
        self.pages = pages


    def title(self, title):
        self.title = self.title
"""



class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


book1 = Book("Tintin och kapten Hadok på resa", "Thintin", 410)
book2 = Book("Tintin och Milo flyger rymdskäpplektioon8", "Thintin", 128)

book1.show_info()
print()
book2.show_info()