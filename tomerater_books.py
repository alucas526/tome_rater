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
