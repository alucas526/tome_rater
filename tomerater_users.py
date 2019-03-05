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

    def validate_email(self, address):
        if address.count(" "):
            return False
        if address.count("@") == 1:
            split_email = address.split("@")
            pre_at = split_email[0]
            post_at = split_email[1]
            if len(pre_at) < 1 or len(post_at) < 1:
                return False
            if pre_at[0] == "." or pre_at[-1] == ".":
                return False
            if post_at[0] != ".":
                dot_count = 0
                for i in range(1, len(post_at) - 2):
                    if post_at[i].count("."):
                        dot_count += 1
                if dot_count != 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def change_email(self, address):
        if not self.validate_email(address):
            return "'{address}' is an invalid email address!".format(address=address)
        else:
            old_email = self.email
            if old_email == address:
                return "No changes made. '{address}' is already the current email address."\
                    .format(address=address)
            else:
                self.email = address
                return "{name}'s email address has been updated from '{old}' to '{new}'."\
                    .format(name=self.name, old=old_email, new=self.email)

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
