# Main file
from guest import *

def main():
    print("Welcome to the pizza calculator!")
    initial = True
    while(initial):
        login = input("Would you like to login or continue as guest? ")
        if login == "login" or login == "Login":
            print("Feature not yet available.")
        elif login == "Guest" or login == "guest":
            initial = False
            guestMain()
        else:
            print("Please enter either 'Login' or 'Guest'")

if __name__ == "__main__":
    main()