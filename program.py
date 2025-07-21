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
        print("")
        print("Hello and welcome {0} to Let's Read, your top fictional book recommendation software.".format(name))
        print()
        print("Below are list of options to choose from.  Enter '1', '2', '3', or '4' to get started")
        

    def display_options(self):
        print("1. Books by Genre")
        print("2. Top Rated Books")
        print("3. Recently Added")
        print("4. Add a book to the library")
        print()
        return 
    
    def get_books_by_genre(self, genre):
        pass

    def top_rated_books_(self):
        pass

    def get_recently_added(self):
        pass

    def add_book(self, user_recommendation):
        pass
        

my_books = Books()
my_books.display_options()
choice = input()

if choice == 1:
    prit()
    print("Thanks for selecting {0}!".format(choice))
elif choice == 2:
    print()
    print("Thanks for selecting {0}!".format(choice))
elif choice == 3:
    print()
    print("Thanks for selecting {0}!".format(choice))
elif choice == 4:
    print()
    print("Thanks for selecting {0}!".format(choice))
else:
    print()
    print("Invalid choice.  Please enter an appropriate option")
    my_books.display_options()
    print()
    choice = input()
