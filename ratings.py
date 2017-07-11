import random

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
        print rest, "is rated at", str(dict_name[rest]) + "."

def validate_rating():
    """Checks user input is an integer and between 1 and 5"""
    
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

    return rating_int

def get_rest_input(dict_name):
    """Takes in user input and adds to dictionary"""

    rest_input = raw_input("Enter a restaurant name: ").title()

    rating_input = validate_rating()
    #adds user inputs to dictionary
    dict_name[rest_input] = rating_input
    return dict_name


def rate_random_rest(dict_name):
    """Chooses random restaurant and lets user re-rate it"""

    sorted_rest = sorted(dict_name)

    random_rest = random.choice(sorted_rest)

    print "Random restaurant is:", random_rest
    print "Its rating is:", dict_name[random_rest]

    rating_input = validate_rating()
    print rating_input

    dict_name[random_rest] = rating_input

    return dict_name



def print_menu():
    """Prints menu and gets user input"""

    read_file("scores.txt")
    print "Welcome to the restaurant rater!"
    print

    while True:

        print
        print "************************"
        print "1. See all restaurants"
        print "2. Add a new restaurant"
        print "3. Rate random restaurant"
        print "Type 'q' to quit"
        print "************************"

        #gets user inputs for the menu
        get_menu_input()

def get_menu_input():
    """Takes in user input and calls appropriate functions"""

    choice = raw_input("> ")

    if choice == '1':
        sort_dict(restaurant_ratings)
    elif choice == '2':
        get_rest_input(restaurant_ratings)
    elif choice == '3':
        rate_random_rest(restaurant_ratings)
    elif choice == 'q':
        exit()
    else:
        print "Enter 1, 2, or q"
        print

print_menu()