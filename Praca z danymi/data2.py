import re
import os

path = os.path.join(os.path.dirname(__file__), "movies.csv")


class Movie():
    def __init__(self, title, description, rating, length):
        self.title = title
        self.description = description
        self.rating = rating
        self.length = length

    def __str__(self):
        return "Title: {0}\nDescription: {1}\nRating: {2}\nLength: {3} min\n".format(self.title, self.description, self.rating, self.length)


def addRecord():
    check = False
    while check == False:
        title = str(input("Enter title of movie\n"))
        description = str(input("Enter description of movie\n"))
        rating = str(input("Enter rating of movie(1->10)\n"))
        length = str(input("Enter length of movie in minutes\n"))

        num_format = re.compile("[0-9]")
        rating_is_number = re.match(num_format, rating)
        length_is_number = re.match(num_format, length)
        if rating_is_number and length_is_number:
            try:
                val = int(rating)
                if val > 0 and val < 11:
                    check = True
                else:
                    print("Rating not in range")
            except ValueError:
                print("Rating or length are not numbers")

        else:
            print("\tERROR: Rating or length are not numbers")

    with open(path, "a+") as f:
        string = title + "," + description + \
            "," + str(rating) + "," + str(length)+"\n"
        f.write(string)


def loadRecords():
    movies = []
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            element = line.split(",")
            movies.append(Movie(str(element[0]), str(
                element[1]), int(element[2]), int(element[3])))
        return movies


def deleteRecord():
    movies = loadRecords()
    if len(movies) > 0:
        movies.pop()
        with open(self.path, "w") as file:
            for i in range(len(movies)):
                string = movies[i].title + "," + movies[i].description + \
                    "," + str(movies[i].rating) + "," + \
                    str(movies[i].length)+"\n"
                file.write(string)
    else:
        print("No movies to delete")


def deleteAll():
    with open(path, "w") as file:
        file.write("")


def options_message():
    print("What do you want to do?")
    print("1. Add record\t2. Delete record\t3. Delete all\t4. Show records\t5. Exit")


def show_movies():
    movies = loadRecords()
    for i in range(len(movies)):
        print(movies[i])


def welcome_message():
    print("Welcome in movie app\n")
    show_movies()
    options_message()


welcome_message()
choice = int(input("(Type 1 or 2 or 3 or 4 or 5)\n"))
while choice != 5:
    if choice == 1:
        addRecord()
    elif choice == 2:
        deleteRecord()
    elif choice == 3:
        deleteAll()
    elif choice == 4:
        show_movies()
    else:
        print("Wrong value typed")
    options_message()
    choice = int(input("(Type 1 or 2 or 3 or 4)\n"))
