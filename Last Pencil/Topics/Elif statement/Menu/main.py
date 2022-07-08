dish_type = input()
if dish_type not in ("pizza", "salad", "soup"):
    print("Sorry, we don't have it in the menu")
elif dish_type == "pizza":
    print("Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy")
elif dish_type == "salad":
    print("Caesar salad, Green salad, Tuna salad, Fruit salad")
elif dish_type == "soup":
    print("Chicken soup, Ramen, Tomato soup, Mushroom cream soup")
