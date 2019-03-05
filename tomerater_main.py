from tomerater_users import *
from tomerater_books import *

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "Welcome to TomeRater!"

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_fiction(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_nonfiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            return "No user was found with an email address of {email}".format(email=email.lower())

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        most_read = 0
        book_title = ""
        for key, value in self.books.items():
            if value > most_read:
                most_read = value
                book_title = key.get_title()
        return "{title} has been read {n} times."\
            .format(title=book_title.title(), n=most_read)

    def highest_rated_book(self):
        highest_avg_rating = 0
        highest_book = ""
        for key in self.books.keys():
            if key.get_avg_rating() > highest_avg_rating:
                highest_avg_rating = key.get_avg_rating()
                highest_book = key.get_title()
        return "{highest_book} is the highest rated of all books, with an average rating of {avg:.2f}"\
            .format(highest_book=highest_book, avg=highest_avg_rating)

    def most_positive_user(self):
        highest_avg_rating = 0
        highest_user = ""
        for user in self.users.values():
            if user.get_avg_rating() > highest_avg_rating:
                highest_avg_rating = user.get_avg_rating()
                highest_user = user.name
        return "{highest_user} is the most positive user, with an average book rating of {avg_rating:.2f}."\
            .format(highest_user=highest_user.title(), avg_rating=highest_avg_rating)
