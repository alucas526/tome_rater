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
            return "{name} has read {n} books and rated {rated} of them, for an average book rating of {avg_rating}".format(name=self.name, n=len(self.books), rated=rated, avg_rating=avg_rating)



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


death_of_a_king = Book("Death Of A King", 9780316332774)
making_work_visible = Book("Making Work Visible: Exposing Time Theft to Optimize Work & Flow", 9781942788157)
kav_and_clay = Fiction("The Amazing Adventures of Kavalier & Clay", "Michael Chabon", 9782002400873)
python_crash_course = NonFiction("Python Crash Course: A Hands-On, Project-Based Introduction to Programming", "Python programming", "beginner", 9781593276034)
alucas = User("Alan Lucas", "alucas@gmail.com")
blucas = User("Alan Lucas", "alucas@gmail.com")
print(alucas)
print(alucas.__eq__(blucas))
print(death_of_a_king)
print(death_of_a_king.add_rating(6))
print(death_of_a_king.add_rating(3))
print(death_of_a_king.add_rating(4))
print(death_of_a_king.add_rating(2))
print(death_of_a_king.add_rating(3))
print(death_of_a_king.ratings)
print(death_of_a_king.get_avg_rating())
print(making_work_visible.get_avg_rating())
print(kav_and_clay)
print(kav_and_clay.get_author())
print(python_crash_course.get_level())
print(python_crash_course.get_subject())
print(python_crash_course)
print(alucas.read_book(kav_and_clay, 4))
print(alucas.read_book(python_crash_course, 3))
print(alucas.read_book(death_of_a_king))
print(alucas.get_avg_rating())
print(python_crash_course.get_avg_rating())
