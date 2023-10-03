# Prompt user for name and greet them using the name entered
userName = input("Please enter your name: ")
print("Hello " + userName + "!")

# Set up loop to repeat the program until the user wishes to stop
keepGoing = "y"
while keepGoing.lower() == "y":

    # Prompt user for the number they wish to have analyzed
    userNumber = int(input("Please enter an integer between 1 and 100 (inclusive):"))

    # Check if entered number is even
    if (userNumber%2) == 0:
        # Determine which range the number falls in and return the appropriate response
        if userNumber > 60:
            print("Even and Greater than 60.")
        elif userNumber > 25:
            print("Even and between 26 and 60 inclusive.")
        else:
            print("Even and less than 25")
    elif userNumber > 60:
        print("Odd and greater than 60")
    else:
        print("Odd and less than 60")

    keepGoing = input("Would you like to continue, " + userName + "? (y/n)")
