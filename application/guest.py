# Guest functions here

def guestMain():
    print("Welcome to guest mode!")
    eaters = True
    while(eaters):
        number = input("How many people in your group want pizza? ")
        confirm = input("To confirm, " + number + " people want pizza? [y/n] ")
        if confirm == "y" or confirm == "yes" or confirm == "Yes":
            eaters = False
        elif confirm != "n":
            print("I will take that as a no...")

    print("Great! Now here is a list of available toppings: ")
    print("Cheese, pepperoni, sausage, onion, green pepper, mushroom, black olive, tomato, basil, ham, pineapple, bacon")
    print("What pizza toppings does the group like?")
    print("Please enter toppings one at a time, hitting ENTER in between toppings. When done, type 'done'.")
    inputOver = False
    while(inputOver == False):
        topping = input()
        print(topping)
        if topping == "done":
            inputOver = True