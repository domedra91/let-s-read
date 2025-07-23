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
    inventory = [["Investing 101","DD","Business", "4", "7"],["How to make a tape dispenser","JD","Drama", "2", "6"],["iPhone","BD","Classical", "4", "7"],["Coins 101","CD","Literature", "5", "4"],["Microscrope","MTD","None", "1", "7"],["Whiteboard","DD","Cool", "2", "1"],["Tory","GD","Business", "3", "6"],["iMAc","HP","Classical", "3", "7"],["Cards","JL","Fun", "5", "4"],["Magic Mouse","TC","Sports", "5", "6"],["Case: Held Alive","PW","sports", "3", "7"],["Thermal Labels","SZ","Literature", "4", "7"],["Classical 101","TM","Science", "4", "7"],["Billiards","JS","Sports", "4", "2"],["Spongebob","DW","Comedy", "5", "7"],["Mixmaster","JP","Sports", "5", "7"]]

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
        genre_first = []
        genre_filtered = []
        for book in my_books.inventory:
            genre_first = ([book[2], book[0], book[1], book[3], book[4]])
            if genre.title() == genre_first[0]:
                genre_filtered.append([book[2], book[0], book[1], book[3], book[4]])
            else:
                continue
        if len(genre_filtered) == 0:
            print("Sorry, we don't have any books to recommend for that genre at the moment")
        else:
            print(genre_filtered)
        return genre_filtered


    def top_rated_books(self):
        print("Here's the top 10 rated books in our database")
        rated_list = []
        for book in my_books.inventory:
            rated_list.append([book[3], book[0], book[1], book[2], book[4]])
        sorted_list = sorted(list, reverse=True)
        print(*sorted_list[:10], sep="\n")
        return sorted_list


    def get_recently_added(self):
        date_first = []
        sorted_date = []
        print("Here the 5 most recently added books:")
        for book in my_books.inventory:
            date_first.append([book[4], book[0], book[1], book[2], book[3]])
        sorted_date = sorted(date_first, reverse=True)
        print(*sorted_date[:5], sep="\n")
        return sorted_date

    def add_book(self, user_book):
        title, author, genre, rating, date = user_book.split(",")
        my_books.inventory.append([title, author, genre, rating, date])
        print("\nYour book has been successfully added.")
        print(*my_books.inventory, sep="\n")
        return my_books.inventory     

    def by_search(self, string):
        search = []
        lower = []
        lower_string = string.lower()
        for book in my_books.inventory:
            lower.append([book[0].lower(), book[1].lower(), book[2].lower(), book[3], book[4]])
        print("Printing results for: " + string + "\n")
        for i in range(0,len(my_books.inventory)):
            if lower_string in lower[i]:
                search.append(my_books.inventory[i])
            else:
                continue 
        if len(search) > 0:
            print(*search, sep="\n")
        else:
            print("Sorry no results found in the database.")
        return search     
        

my_books = Books()
my_books.display_options()
choice = int(input())

while True:
    if choice == 1:
        print("Thanks for selecting {0}!\nWhat genre would you like to search by?\n".format(choice))
        user_genre = input()
        genre_titled = user_genre.title()
        my_books.get_books_by_genre(genre_titled)
        break

    elif choice == 2:
        print("Thanks for selecting {0}!\n".format(choice))
        my_books.top_rated_books()
        break

    elif choice == 3:
        print("Thanks for selecting {0}!\n".format(choice))
        my_books.get_recently_added()
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
            break

    elif choice == 5:
        print("Thanks for selecting {0}!\n".format(choice))
        print("Please enter a keyword, title, genre, or author to search database:")
        user_input = input()
        my_books.by_search(user_input)
        break

    elif choice == 6:
        print("Have a nice day!\n".format(choice))
        break

    else:
        print("Invalid choice.  Please enter an appropriate option\n")
        my_books.display_options()
        choice = int(input())

