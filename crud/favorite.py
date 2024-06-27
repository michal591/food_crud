def favorite_food(my_foods):
    print("my favorite foods:")
    for food in my_foods:
        if food["favorite"] == True:
            print(food)
