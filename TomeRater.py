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


alucas = User("Alan Lucas", "alucas@gmail.com")
blucas = User("Alan Lucas", "alucas@gmail.com")
print(alucas)
print(alucas.__eq__(blucas))
