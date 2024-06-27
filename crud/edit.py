from crud.crud import get_list


def edit_food(my_foods):
    get_list(my_foods)
    food_to_edit = input("what's the name of food that you want to edit? ")
    food_found = False
    for food in my_foods:
        if food["name"] == food_to_edit:
            food_found = True
            key_to_edit = input(
                "what do you want to edit- name/ color/ group/ favorite? "
            )
            new_value = input("what is the new value? ")
            if key_to_edit == "name":
                food["name"] = new_value
                print(f"the name of {food_to_edit} has been update to {new_value}")
            elif key_to_edit == "color":
                food["color"] = new_value
                print(f"the color of {food_to_edit} has been update to {new_value}")
            elif key_to_edit == "group":
                food["group"] = new_value
                print(f"the group of {food_to_edit} has been update to {new_value}")
            elif key_to_edit == "favorite":
                food["favorite"] = new_value
                print(f"favorite has been update to {new_value}")
    if not food_found:
        print(f"the food {food_to_edit} is not on the list")
