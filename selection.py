from crud.crud import get_list, add_food, delete_food
from crud.search import search_food
from crud.favorite import favorite_food
from crud.edit import edit_food


def selection(my_foods, select):
    if select == 1:
        get_list(my_foods)
    elif select == 2:
        add_food(my_foods)
    elif select == 3:
        delete_food(my_foods)
    elif select == 4:
        edit_food(my_foods)
    elif select == 5:
        search_food(my_foods)
    elif select == 6:
        favorite_food(my_foods)
