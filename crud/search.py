def search_food(my_foods):
    key_to_search = input("what do you want to search- name/ color/ group? ")
    value_to_search = input("What are the first letters you want to find? ")

    if key_to_search == "name":
        name_search = [
            food
            for food in my_foods
            if food["name"].lower().startswith(value_to_search)
        ]
        if name_search:
            print(f"the food found starting with {value_to_search}: {name_search}")
        else:
            print(f"no foods found starting with {value_to_search}")

    elif key_to_search == "color":
        color_search = [
            food
            for food in my_foods
            if food["color"].lower().startswith(value_to_search)
        ]
        if color_search:
            print(f"the food found starting with {value_to_search}: {color_search}")
        else:
            print(f"no foods found starting with {value_to_search}")

    elif key_to_search == "group":
        group_search = [
            food
            for food in my_foods
            if food["group"].lower().startswith(value_to_search)
        ]
        if group_search:
            print(f"the food found starting with {value_to_search}: {group_search}")
        else:
            print(f"no foods found starting with {value_to_search}")
