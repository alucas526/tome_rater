class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "{name} has read {books} books and can be reached at {email}.".format(name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return "This is the same user."

    def get_email(self):
        return self.email

    def change_email(self, address):
        old_email = self.email
        if address.count("@") == 0 or address.count(".") == 0:
            return "{address} is not a valid email address. Please try again.".format(address=address)
        if old_email == address:
            return "No changes made. {address} is already the current email address.".format(address=address)
        else:
            self.email = address
            return "Your email address has been updated from {old} to {new}.".format(old=old_email, new=self.email)

    def read_book(self, book, rating=None):
        self.books.update({book: rating})
        if rating is not None:
            book.ratings.append(rating)

    def get_avg_rating(self):
        total_ratings = 0
        rated = 0
        avg_rating = 0
        if len(self.books) > 0:
            for rating in self.books.values():
                if rating is not None:
                    total_ratings += rating
                    rated += 1
                avg_rating = total_ratings / rated
            return "{name} has read {n} book(s) and rated {rated} of them, for an average book rating of {avg_rating}".format(name=self.name, n=len(self.books), rated=rated, avg_rating=avg_rating)


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return "\"{title}\", ISBN {isbn}".format(title=self.title, isbn=self.isbn)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return "This is the same book."

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        old_isbn = self.isbn
        if old_isbn == isbn:
            return "No changes made. {isbn} is already the current ISBN.".format(isbn=isbn)
        else:
            self.isbn = isbn
            return "The ISBN has been updated from {old} to {new}.".format(old=old_isbn, new=self.isbn)

    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("{rating} is not a valid rating. Please enter a number between 0 and 4.".format(rating=rating))

    def get_avg_rating(self):
        total_ratings = 0
        if len(self.ratings) > 0:
            for rating in self.ratings:
                total_ratings += rating
            avg_rating = total_ratings / len(self.ratings)
            return "\"{title}\" has {n} rating(s). The average rating is {rating} out of 4 stars.".format(title=self.title, n=len(self.ratings), rating=avg_rating)
        else:
            return "\"{title}\" does not have any ratings yet.".format(title=self.title)


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "\"{title}\" by {author}".format(title=self.title, author=self.author)

    def get_author(self):
        return self.author


class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "\"{title}\", a {level} manual on {subject}.".format(title=self.title, level=self.level, subject=self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "Welcome to TomeRater!"

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            if User.get_email(email):
                User.read_book(book, rating)
                Book.add_rating(book, rating)
            # if book in self.books:
        else:
            return "No user with email address {email}".format(email=email)

    def add_user(self, name, email, books=None):
        User(name, email)
        if books is not None:
            for book in books:
                self.add_book_to_user(book, email)



# user1 = User("Bob", "bob@bob.com")
# book1 = Fiction("It", "Stephen King", 9781501175466)
# print(user1.read_book(book1, 3.5))
# print(user1.get_avg_rating())
# print(book1.get_avg_rating())
# print(TomeRater().create_book("This", 5645484654))
# print(TomeRater().create_novel("Hey", "Bob", 243572345897))
# print(TomeRater().add_book_to_user("It", user1.email))
# TomeRater().users["bob@bob.com"] = "Bob Smith"
# print(TomeRater().users)
# print(TomeRater().add_book_to_user(book1.title, user1.email))
#
# xusers = {}
# xusers["bob@bob.com"] = "Bob Simon"
# print(xusers)
