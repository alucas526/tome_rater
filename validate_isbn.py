from tomerater_main import *

isbn_validation = TomeRater()

book1 = isbn_validation.create_book("Society of Mind", 9780671657130)
novel1 = isbn_validation.create_fiction("Alice In Wonderland", "Lewis Carroll", 9781503250215)
novel1.set_isbn(9781536831139)
nonfiction1 = isbn_validation.create_nonfiction("Automate the Boring Stuff", "Python", "beginner", 9781593275990)
nonfiction2 = isbn_validation.create_nonfiction("Computing Machinery and Intelligence", "AI", "advanced", 9780262560925)
novel2 = isbn_validation.create_fiction("The Diamond Age", "Neal Stephenson", 9780553380965)
novel3 = isbn_validation.create_fiction("There Will Come Soft Rains", "Ray Bradbury", 9780895989628)
novel4 = isbn_validation.create_fiction("It", "Stephen King", 2234756)

print(nonfiction1.get_isbn())

print(nonfiction1.set_isbn("beset"))
print(nonfiction1.set_isbn(123))
print(nonfiction1.set_isbn(12345677654321))
print(nonfiction1.set_isbn(9781593275990))
print(nonfiction1.set_isbn(1234567890))
print(nonfiction1.set_isbn(1029384756098))
print(novel4)
