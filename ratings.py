"""Restaurant rating lister."""

rest_output = {}

def sort_dict(dict_name):
    """Sorts and outputs a list of restaurants and their ratings"""

    sorted_rest = sorted(dict_name)

    for rest in sorted_rest:
        print rest, "is rated at", dict_name[rest] + "."


def get_input(dict_name):
    """Takes in user input and adds to dictionary"""

    rest_input = raw_input("Enter a restaurant name: ").title()

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


    dict_name[rest_input] = rating_input
    return dict_name


def restaurant_ratings(filename):
    """Reads and sorts file"""

    read_file(filename)

    sort_dict(rest_output)

    restaurant_file.close()

    rest_output = get_input(rest_output)

    sort_dict(rest_output)

def read_file(filename):

    restaurant_file = open(filename)

    for line in restaurant_file:
        line = line.rstrip()
        rest_and_ratings = line.split(":")
        rest_output[rest_and_ratings[0]] = rest_and_ratings[1]


print "Welcome to the restaurant rater!"
print

while True:

    print
    print "************************"
    print "1. See all restaurants"
    print "2. Add a new restaurant"
    print "Type 'q' to quit"
    print "************************"

    choice = raw_input("> ")

    if choice == '1':
        read_file("scores.txt")
        sort_dict(rest_output)
    elif choice == '2':
        get_input(rest_output)
    elif choice == 'q':
        exit()
    else:
        print "Enter 1, 2, or q"
        print 
#restaurant_ratings("scores.txt")