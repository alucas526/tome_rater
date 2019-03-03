class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "{name} has read {num} book(s) and can be reached at {email}".format(name=self.name,
                                                                                    num=len(self.books),
                                                                                    email=self.email)

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return "{self_name} and {other_name} are the same user!".format(self_name=self.name,
                                                                            other_name=other_user.name)
        else:
            return "{self_name} and {other_name} are not the same user.".format(self_name=self.name,
                                                                                other_name=other_user.name)

    def get_email(self):
        return "{name}'s email address is {email}.".format(name=self.name, email=self.email)

    def change_email(self, new_email):
        current_email = self.email
        if new_email != self.email:
            self.email = new_email
            return "{name}'s email address has been changed from {old} to {new}.".format(name=self.name,
                                                                                         old=current_email,
                                                                                         new=self.email)
        else:
            return "{name}'s email address is already {new} and has not been changed.".format(name=self.name,
                                                                                              new=new_email)

    def read_book(self, book, rating=None):
        if rating is not None:
            if 0 <= rating <= 4:
                self.books.update({book: rating})
                return "{name} read \"{title}\" and gave it a rating of {rating}".format(name=self.name,
                                                                                         title=book.title,
                                                                                         rating=rating)
            else:
                return "{rating} is not a valid rating! Rating must be between 0 and 4.".format(rating=rating)
        else:
            self.books.update({book: rating})
            return "{name} read \"{title}\". No rating was provided.".format(name=self.name, title=book.title)

    def get_avg_rating(self):
        total_rating = 0
        total_books = 0
        rated_books = 0
        if len(self.books) > 0:
            for book_rating in self.books.values():
                total_books += 1
                if book_rating is not None:
                    total_rating += book_rating
                    rated_books += 1
            if rated_books > 0:
                avg_rating = total_rating / rated_books
                return "{name} has read {num_books}, and rated {rated_books}, book(s). The average rating is " \
                       "{avg_rating:.2f}".format(name=self.name, num_books=total_books, rated_books=rated_books,
                                                 avg_rating=avg_rating)
            else:
                return "{name} has read {num_books} but has not rated any of them.".format(name=self.name,
                                                                                           num_books=total_books)
        else:
            return "{name} has not read any books!".format(name=self.name)


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return "\"{title}\", {isbn}".format(title=self.title, isbn=self.isbn)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return "\"{self_title}\" and \"{other_title}\" are the same book!".format(self_title=self.title,
                                                                                      other_title=other_book.title)
        else:
            return "\"{self_title}\" and \"{other_title}\" are not the same book.".format(self_title=self.title,
                                                                                          other_title=other_book.title)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return "The name of this book is \"{title}\".".format(title=self.title)

    def get_isbn(self):
        return "{isbn} is the ISBN for \"{title}\".".format(title=self.title, isbn=self.isbn)

    def set_isbn(self, new_isbn):
        current_isbn = self.isbn
        if new_isbn != self.isbn:
            self.isbn = new_isbn
            return "The ISBN for \"{title}\" has been changed from {old} to {new}.".format(title=self.title,
                                                                                           old=current_isbn,
                                                                                           new=self.isbn)
        else:
            return "The ISBN for \"{title}\" is already {isbn} and has not been changed.".format(title=self.title,
                                                                                                 isbn=self.isbn)

    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
            return "A rating of {rating} has been added to \"{title}\".".format(rating=rating, title=self.title)
        else:
            return "{rating} is not a valid rating! Rating must be between 0 and 4.".format(rating=rating)

    def get_avg_rating(self):
        total_rating = 0
        if len(self.ratings) > 0:
            for rating in self.ratings:
                total_rating += rating
            avg_rating = total_rating / len(self.ratings)
            return "{title} has {num_ratings} rating(s) and an average rating of {avg_rating:.2f}."\
                .format(title=self.title, num_ratings=len(self.ratings), avg_rating=avg_rating)
        else:
            return "{title} does not have any ratings!".format(title=self.title)


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "\"{title}\" is a work of fiction by {author}".format(title=self.title.title(), author=self.author)

    def get_author(self):
        return "\"{title}\" was written by {author}.".format(title=self.title.title(), author=self.author)


class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "\"{title}\" is a {level}-level manual on {subject}.".format(title=self.title.title(),
                                                                            level=self.level, subject=self.subject)

    def get_subject(self):
        return "{subject} is the subject of \"{title}\".".format(subject=self.subject.title(), title=self.title.title())

    def get_level(self):
        return "\"{title}\" is a {level}-level book.".format(title=self.title.title(), level=self.level)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "Welcome to TomeRater!"

    def create_book(self, title, isbn):
        self.books[title, isbn] = 0
        return Book(title, isbn)

    def create_fiction(self, title, author, isbn):
        self.books[title, isbn] = 0
        return Fiction(title, author, isbn)

    def create_nonfiction(self, title, subjec, level, isbn):
        self.books[title, isbn] = 0
        return NonFiction(title, subjec, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            User.read_book(book, rating)
            Book.add_rating(book, rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            return "No user with email {email}!".format(email=email)

    def add_user(self, name, email, user_books=None):
        User(name, email)
        self.users[name] = email
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email, rating=None)

    def print_catalog(self):
        pass


# tomerater = TomeRater()
# print(tomerater.add_user("Bob", "bob@bob.com"))
# print(tomerater.add_user("Larry", "x@y.com"))
# print(tomerater.books)
# print(tomerater.users)
# print(len(tomerater.users))
