def get_list(my_foods):
    for food in my_foods:
        print(f"my food is: {food}")


def add_food(my_foods: list):
    new_name = input("which food you want to add? ")
    new_color = input("what is the color of this food? ")
    new_group = input("Which food group does the food belong to? ")
    new_favorite = input("is this food your favorite? (write true/ false)")
    new_food = {
        "name": new_name,
        "color": new_color,
        "group": new_group,
        "favorite": new_favorite,
    }
    my_foods.append(new_food)
    print(f"the food added to my food: {new_food}")


def delete_food(my_foods: list):
    get_list(my_foods)
    food_to_delete = input("what's the name of food that you want to delete? ")
    for food in my_foods:
        if food["name"] == food_to_delete:
            my_foods.remove(food)
            print(f"the food: {food} has been removed from the list")
        else:
            print(f"the food: {food} is not on the list")



