class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

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

    def __repr__(self):
        return "{name} has read {books} books and can be reached at {email}.".format(name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return "This is the same user."


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

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
        if 0 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("{rating} is not a valid rating. Please enter a number between 0 and 5.".format(rating=rating))

    def avg_rating(self):
        total_ratings = 0
        if len(self.ratings) > 0:
            for rating in self.ratings:
                total_ratings += rating
            avg_rating = total_ratings / len(self.ratings)
            return "The average rating for \"{title}\" is {rating}".format(title=self.title, rating=avg_rating)
        else:
            return "\"{title}\" does not have any ratings yet.".format(title=self.title)

    def __repr__(self):
        return "\"{title}\", ISBN {isbn}".format(title=self.title, isbn=self.isbn)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return "This is the same book."


alucas = User("Alan Lucas", "alucas@gmail.com")
blucas = User("Alan Lucas", "alucas@gmail.com")
print(alucas)
print(alucas.__eq__(blucas))
death_of_a_king = Book("Death Of A King", 9780316332774)
print(death_of_a_king)
print(death_of_a_king.add_rating(6))
print(death_of_a_king.add_rating(3))
print(death_of_a_king.add_rating(4))
print(death_of_a_king.add_rating(5))
print(death_of_a_king.add_rating(3))
print(death_of_a_king.ratings)
print(death_of_a_king.avg_rating())
making_work_visible = Book("Making Work Visible: Exposing Time Theft to Optimize Work & Flow", 9781942788157)
print(making_work_visible.avg_rating())