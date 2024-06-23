# Guest functions here

def guestMain():
    pizzaToppings = ["cheese", "pepperoni", "sausage", "onion", "green pepper", "black olive", "tomato", "basil", "ham", "pineapple",
                "bacon", "mushroom"] 
    print("Welcome to guest mode!")
    eaters = True
    while(eaters):
        number = int(input("How many people in your group want pizza? "))
        confirm = input("To confirm, " + str(number) + " people want pizza? [y/n] ")
        if confirm == "y" or confirm == "yes" or confirm == "Yes":
            eaters = False
        elif confirm != "n":
            print("I will take that as a no...")

    print()
    print("Great! Now here is a list of available toppings: ")
    print("Cheese, pepperoni, sausage, onion, green pepper, mushroom, black olive, tomato, basil, ham, pineapple, bacon")
    print()
    print("What pizza toppings does the group like?")
    print("Please enter toppings one at a time, hitting ENTER in between toppings. When done, type 'done'.")
    inputOver = False
    userToppings = []
    while(inputOver == False):
        proper = False
        topping = input("> ")
        for i in pizzaToppings:
            if topping == i:
                proper = True
                userToppings.append(topping)
        if topping == "done":
            if len(userToppings) == 0:
                print("You must choose at least one topping!")
            else:
                inputOver = True
        elif proper == False:
            print("That is not one of the listed pizza toppings.")
    print("You have selected the following toppings:")
    print(*userToppings, sep = ", ")
    print()
    print("Calculating...")

    if number < 8:
        calculation(0, number, userToppings)
    elif (number % 8) == 0:
        calculation(number, 0, userToppings)
    else:
        remainder = number%8
        calculation(number-remainder, remainder, userToppings)

def calculation(multiple, remainder, toppings):
    easyLarge = multiple / 8
    largeZa = int(easyLarge*3)

    # remaining slices from left over people
    slices = remainder*3
    smallZa = 0

    if (slices%8) == 0:
        largeZa += slices/8
    else:
        newRemainder = slices%8
        largeZa += int((slices-newRemainder)/8)
        if newRemainder < 5:
            smallZa += 1
        else:
            largeZa += 1
    
    pizzaList = []

    if len(toppings) < (smallZa + largeZa):
        # maybe combine toppings? idk
        smallZaStr = ""
        for x in toppings:
            pizza = "A large " + x + " pizza"
            pizzaList.append(pizza)
        remaining = (smallZa + largeZa) - len(toppings)
        if smallZa == 1:
            if "cheese" in toppings:
                smallZaStr = "A small cheese pizza"
                #pizzaList.append("A small cheese pizza")
                #toppings.remove("cheese")
            else:
                smallZaStr = "A small " + toppings[0] + " pizza"
                #toppings.remove(toppings[0])
            remaining -= 1
        while remaining > 0:
            for x in toppings:
                if remaining == 0:
                    break
                else:
                    pizza = "A large " + x + " pizza"
                    pizzaList.append(pizza)
                    remaining -= 1
        if len(smallZaStr) > 0:
            pizzaList.append(smallZaStr)

    elif len(toppings) == (smallZa + largeZa):
        # assign evenly
        if smallZa == 1:
            if "cheese" in toppings:
                pizzaList.append("A small cheese pizza")
                toppings.remove("cheese")
            for x in toppings:
                pizza = "A large " + x + " pizza"
                pizzaList.append(pizza)
        else:
            for x in toppings:
                pizza = "A large " + x + " pizza"
                pizzaList.append(pizza)
    else:
        print("more")

    print("You should order: ")
    if smallZa == 0:
        if largeZa == 1:
            print(str(largeZa) + " Large Pizza")
        else:
            print(str(largeZa) + " Large Pizzas")
    else:
        if largeZa == 1:
            print(str(largeZa) + " Large Pizza and " + str(smallZa) + " Small Pizza")
        else:
            print(str(largeZa) + " Large Pizzas and " + str(smallZa) + " Small Pizza")
    print(*pizzaList, sep = ", ")