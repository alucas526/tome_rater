class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = []

    def __repr__(self):
        return "{name} has read {num} books and can be reached at {email}."\
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


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return "\"{title}\", {isbn}".format(title=self.title.title(), isbn=self.isbn)

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
                return "A rating of {rating} has been added to \"{title}\"."\
                    .format(rating=rating, title=self.title.title())
            else:
                return "{rating} is not a valid rating. Rating must be between 0 and 4."\
                    .format(rating=rating)
        else:
            return "No rating added to \"{title}\".".format(title=self.title.title())


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "\"{title}\", by {author}"\
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
        pass

    def get_level(self):
        pass


book1 = Book("It", 234524352)
book2 = Book("where the wild things are", 234598243895)
book3 = Book("where the wild things are", 234598243895)
fiction1 = Fiction("Hello", "Walter Walter", 243587987234)
nonfiction1 = NonFiction("do all of the things", "speed reading", "INTERMEDIATE", 2348957890243)
bob = User("Bob", "bob@bob.com")
bob2 = User("Bob", "bob@robert.com")
print(bob.get_email())
print(bob.change_email("bob@robert.com"))
print(bob)
print(book2.add_rating(5))
print(book2.add_rating(None))
print(book2.add_rating(4))
print(book2.add_rating(3))
print(book2.ratings)
print(book2.__eq__(book3))
print(bob.__eq__(bob2))
print(fiction1.get_author())
print(fiction1)
print(nonfiction1)
