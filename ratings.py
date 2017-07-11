"""Restaurant rating lister."""

restaurant_ratings = {}


def read_file(filename):
    """Reads a file and stores info in a dictionary"""

    restaurant_file = open(filename)

    #loop through each line in file
    for line in restaurant_file:
        #strip whitespace at end of line
        line = line.rstrip()
        #split line and store in list using ":"" as delimiter
        rest_and_ratings = line.split(":")
        rest_name = rest_and_ratings[0]
        rating_num = rest_and_ratings[1]
        #add restaurant name and rating to dictionary
        restaurant_ratings[rest_name] = rating_num

    restaurant_file.close()

def sort_dict(dict_name):
    """Sorts and outputs a list of restaurants and their ratings"""

    #alphabetically sorts restaurant names and stores in list
    sorted_rest = sorted(dict_name)

    #loops through list, prints restaurant name and its rating
    for rest in sorted_rest:
        print rest, "is rated at", dict_name[rest] + "."


def get_rest_input(dict_name):
    """Takes in user input and adds to dictionary"""

    rest_input = raw_input("Enter a restaurant name: ").title()

    #validate user input, checks if rating is an integer and between 1 and 5
    while True:
        try:
            rating_input = raw_input("Enter a rating: ")
            rating_int = int(rating_input)
            if rating_int <=5 and rating_int >= 1:
                break
            else:
                print "Please enter a number between 1 and 5: "
        except:
            print "Please enter a number between 1 and 5: "

    #adds user inputs to dictionary
    dict_name[rest_input] = rating_input
    return dict_name


def print_menu():
    """Prints menu and gets user input"""

    print "Welcome to the restaurant rater!"
    print

    while True:

        print
        print "************************"
        print "1. See all restaurants"
        print "2. Add a new restaurant"
        print "Type 'q' to quit"
        print "************************"

        #gets user inputs for the menu
        get_menu_input()

def get_menu_input():
    """Takes in user input and calls appropriate functions"""

    choice = raw_input("> ")

    if choice == '1':
        read_file("scores.txt")
        sort_dict(restaurant_ratings)
    elif choice == '2':
        get_rest_input(restaurant_ratings)
    elif choice == 'q':
        exit()
    else:
        print "Enter 1, 2, or q"
        print

print_menu()