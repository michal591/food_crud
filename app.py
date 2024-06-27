from selection import selection


my_foods = [
    {"name": "apple", "color": "red", "group": "fruits", "favorite": True},
    {
        "name": "chicken",
        "color": "white",
        "group": "meat",
        "favorite": True,
    },
    {
        "name": "rice",
        "color": "white",
        "group": "extras",
        "favorite": False,
    },
]


def menu():
    load(my_foods)
    while True:
        print("1- get the food list ")
        print("2- add a food to the food list ")
        print("3- delete a food from the food list ")
        print("4- edit a food in the food list ")
        print("5- search a food from the food list ")
        print("6- get the favorite foods ")
        print("7- exit")
        select = int(input("enter your choose: "))
        if select == 7:
            break
        selection(my_foods, select)
        save(my_foods)


if __name__ == "__main__":
    menu()
