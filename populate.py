from tomerater_main import *

Tome_Rater = TomeRater()

# Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 9780671657130)
novel1 = Tome_Rater.create_fiction("Alice In Wonderland", "Lewis Carroll", 9781503250215)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_nonfiction("Automate the Boring Stuff", "Python", "beginner", 9781593275990)
nonfiction2 = Tome_Rater.create_nonfiction("Computing Machinery and Intelligence", "AI", "advanced", 9780262560925)
novel2 = Tome_Rater.create_fiction("The Diamond Age", "Neal Stephenson", 9780553380965)
novel3 = Tome_Rater.create_fiction("There Will Come Soft Rains", "Ray Bradbury", 9780895989628)
novel4 = Tome_Rater.create_fiction("It", "Stephen King", 2234756)

# Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

# Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", [book1, novel1, nonfiction1])

# Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

# Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
