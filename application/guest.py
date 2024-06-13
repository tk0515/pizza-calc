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

    print("Great!")