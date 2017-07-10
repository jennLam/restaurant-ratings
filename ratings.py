"""Restaurant rating lister."""


# put your code here
def restaurant_ratings(filename):
    """Outputs a list of restaurants and their ratings"""

    restaurant_file = open(filename)

    rest_output = {}

    for line in restaurant_file:
        line = line.rstrip()
        rest_and_ratings = line.split(":")
        rest_output[rest_and_ratings[0]] = rest_and_ratings[1]

    sorted_rest = sorted(rest_output)

    for rest in sorted_rest:
        print rest, "is rated at", rest_output[rest] + "."

    restaurant_file.close()

restaurant_ratings("scores.txt")