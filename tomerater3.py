class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "{name} has read {num} book(s) and can be reached at {email}."\
            .format(name=self.name, num=len(self.books), email=self.email)

    def __eq__(self, other_user):
        if other_user.name == self.name and other_user.email == self.email:
            return True
        else:
            return False

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "{name}'s email address has been changed to {new}."\
            .format(name=self.name, new=self.email)

    def read_book(self, book, rating=None):
        self.books.update({book: rating})
        if rating is not None:
            return "{name} read \"{book}\" and gave it a rating of {rating:.2f}."\
                .format(name=self.name.title(), rating=rating, book=book.title.title())
        else:
            return "{name} read \"{book}\", but did not provide a rating."\
                .format(name=self.name.title(), book=book.title.title())

    def get_avg_rating(self):
        total_rating = 0
        rated_books = 0
        if len(self.books) > 0:
            for rating in self.books.values():
                if rating is not None:
                    total_rating += rating
                    rated_books += 1
            if total_rating > 0:
                avg_rating = total_rating / rated_books
                return avg_rating
            else:
                return "{name} has read {read} book(s), but hasn't provided any rating(s)."\
                    .format(name=self.name.title(), read=len(self.books))
        else:
            return "{name} has not rated any books.".format(name=self.name)


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "\"{title}\" is a book with an ISBN of {isbn}.".format(title=self.title.title(), isbn=self.isbn)

    def __eq__(self, other_book):
        if other_book.title == self.title and other_book.isbn == self.isbn:
            return True
        else:
            return False

    def get_title(self):
        return "\"{title}\"".format(title=self.title.title())

    def get_isbn(self):
        return "{isbn} is the ISBN of \"{title}\"."\
            .format(isbn=self.isbn, title=self.title.title())

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "{isbn} is the new ISBN for \"{title}\"."\
            .format(isbn=self.isbn, title=self.title.title())

    def add_rating(self, rating):
        if rating is not None:
            if 0 <= rating <= 4:
                self.ratings.append(rating)
                return "A rating of {rating:.2f} has been added to \"{title}\"."\
                    .format(rating=rating, title=self.title.title())
            else:
                return "{rating} is not a valid rating. Rating must be between 0 and 4."\
                    .format(rating=rating)
        else:
            return "No rating added to \"{title}\".".format(title=self.title.title())

    def get_avg_rating(self):
        if len(self.ratings) > 0:
            total_rating = 0
            for rating in self.ratings:
                total_rating += rating
            avg_rating = total_rating / len(self.ratings)
            return avg_rating
        else:
            return "\"{title}\" does not have any ratings."\
                .format(title=self.title)


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "\"{title}\" is a work of fiction by {author}."\
            .format(title=self.title.title(), author=self.author)

    def get_author(self):
        return "{author} is the author of \"{title}\".".format(author=self.author, title=self.title.title())


class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "\"{title}\" is a(n) {level}-level manual on {subject}."\
            .format(title=self.title.title(), level=self.level.lower(), subject=self.subject.title())

    def get_subject(self):
        return "The subject of \"{title}\" is {subject}."\
            .format(title=self.title.title(), subject=self.subject)

    def get_level(self):
        return "\"{title}\" is a(n) {level}-level book.".format(title=self.title.title(), level=self.level.lower())


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

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
        return "{title} has been read {n} times.".format(title=book_title.title(), n=most_read)

    # def highest_rated_book(self):
    #     highest_avg_rating = 0
    #     highest_book = ""
    #     for key in self.books.keys():
    #         print(key)
    #         if key.get_avg_rating() > highest_avg_rating:
    #             highest_avg_rating = key.get_avg_rating
    #             highest_book = key.get_title()
    #     return highest_book
    #
    def most_positive_user(self):
        highest_avg_rating = 0
        highest_user = ""
        for user in self.users.values():
            if user.get_avg_rating() > highest_avg_rating:
                highest_avg_rating = user.get_avg_rating()
                highest_user = user.name
        return "{highest_user} is the most positive user with an average book rating of {avg_rating:.2f}."\
            .format(highest_user=highest_user.title(), avg_rating=highest_avg_rating)



# book1 = Book("It", 234524352)
# book2 = Book("where the wild things are", 234598243895)
# book3 = Book("where the wild things are", 234598243895)
# fiction1 = Fiction("Hello", "Walter Walter", 243587987234)
# nonfiction1 = NonFiction("do all of the things", "speed reading", "INTERMEDIATE", 2348957890243)
# bob = User("Bob", "bob@bob.com")
# bob2 = User("Bob Two", "bob@robert.com")
# print(bob.get_email())
# print(bob.change_email("bob@robert.com"))
# print(bob)
# print(book2.add_rating(5))
# print(book2.add_rating(None))
# print(book2.add_rating(4))
# print(book2.add_rating(3))
# print(book2.ratings)
# print(book2.__eq__(book3))
# print(bob.__eq__(bob2))
# print(fiction1.get_author())
# print(fiction1)
# print(nonfiction1)
# print(bob.read_book(book1, 4))
# print(bob.read_book(book2, 3))
# print(bob.read_book(fiction1))
# print(bob.read_book(nonfiction1, 4))
# print(bob.get_avg_rating())
# print(bob2.read_book(fiction1))
# print(bob2.get_avg_rating())
# print(nonfiction1.add_rating(4))
# print(nonfiction1.get_avg_rating())
# print(fiction1.get_avg_rating())
