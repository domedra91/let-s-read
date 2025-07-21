#let's read!
#introduction to software

print("\n" * 2)
print("------------------------")
print("       _        _       ")
print("      |_|------|_|      ")
print("           |            ")
print("                        ")
print("------------------------")
print("\n" * 2)

class Books:
    inventory = [["Investing 101","DD","Business", "4", "7"]]

    def __init__(self):
        name = input("Please enter your name \n")
        print("Hello and welcome {0} to 'Let's Read', your top fictional book recommendation software.\n".format(name))
        print("Below are list of options to choose from.  Enter '1', '2', '3', or '4' to get started\n")
        

    def display_options(self):
        print("1. Books by Genre")
        print("2. Top Rated Books")
        print("3. Recently Added")
        print("4. Add a book to the library")
        print("5. By search")
        print("6. Quit\n")
        return 
    
    def get_books_by_genre(self, genre):
        print("thanks for playing the game")
        return 

    def top_rated_books_(self):
        pass

    def get_recently_added(self):
        pass

    def add_book(self, user_book):
        title, author, genre, rating, date = user_book.split(",")
        my_books.inventory.append([title, author, genre, rating, date])
        print("\nYour book has been successfully added.")
        print(*my_books.inventory, sep="\n")
        return my_books.inventory     

    def by_search(self, string):
        pass
        

my_books = Books()
my_books.display_options()
choice = int(input())

while True:
    if choice == 1:
        print("Thanks for selecting {0}!\nWhat genre would you like to search by?\n".format(choice))
        user_genre = input()
        genre_titled = user_genre.title()
        print("'{0}'-books are below".format(genre_titled))
        my_books.get_books_by_genre(genre_titled)
        break

    elif choice == 2:
        print("Thanks for selecting {0}!\n".format(choice))
        break

    elif choice == 3:
        print("Thanks for selecting {0}!\n".format(choice))
        break
    
    elif choice == 4:
        print("Thanks for selecting {0}!\n".format(choice))
        print("Please add book in the following order, separated by commas: title, author, genre, rating, today's month number")
        user_book = input()
        user_book_titled = user_book.title()
        my_books.add_book(user_book_titled)
        print("\nDo you wish to add another book, enter 'y' for yes, 'n' to quit")
        choice2 = input()
        choice2 = choice2.lower()
        if choice2 == 'y':
            print("Please add book in the following order, separated by commas: title, author, genre, rating, today's month number")
            user_book = input()
            user_book_titled = user_book.title()
            my_books.add_book(user_book_titled)
            print("\nDo you wish to add another book, enter 'y' for yes, 'n' to quit")
            choice2 = input()
            choice2 = choice2.lower()
        else:
            choice = 0
            my_books.display_options()
            choice = int(input())
            break

    elif choice == 5:
        print("Thanks for selecting {0}!\n".format(choice))
        break

    elif choice == 6:
        print("Have a nice day! {0}!\n".format(choice))
        break

    else:
        print("Invalid choice.  Please enter an appropriate option\n")
        my_books.display_options()
        choice = int(input())

