#let's read!
#introduction to software

print("------------------------")
print("       _        _       ")
print("      |_|------|_|      ")
print("           |            ")
print("                        ")
print("------------------------")
print()
print()

class Books:
    def __init__(self):
        name = input("Please enter your name \n")
        print("Hello and welcome {0} to Let's Read, your top book recommendation software.  Below are list of options.  Please review to get started".format(name))
        

    def display_options(self):
        print("1. Books by Genre")
        print("2. Top Rated Books")
        print("3. Recently Added")
        print("4. Add a book to the library")
        print()
        choice = input("Enter choice: \n")
        print("Thanks for selecting option #{0}!".format(choice))

    
    
    def get_books_by_genre():
        pass

    def top_rated_books_():
        pass

    def get_recently_added():
        pass

    def add_book():
        pass
        

my_books = Books()
my_books.display_options()