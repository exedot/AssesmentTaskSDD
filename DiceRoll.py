def start():
    import random

    # Assigns die to variables "rolla" & "rollb"
    rolla = random.randint(1,6)
    rollb = random.randint(1,6)

    # Tells program which ASCII to embed
    def aroll():
            if rolla == 1:
                print(a1)
            elif rolla == 2:
                print(a2)
            elif rolla == 3:
                print(a3)
            elif rolla == 4:
                print(a4)
            elif rolla == 5:
                print(a5)
            elif rolla == 6:
                print(a6)
    def broll():
            if rollb == 1:
                print(a1)
            elif rollb == 2:
                print(a2)
            elif rollb == 3:
                print(a3)
            elif rollb == 4:
                print(a4)
            elif rollb == 5:
                print(a5)
            elif rollb == 6:
                print(a6)

    # Colour scheme
    white = str("\u001b[37m")
    yellow = str("\u001b[33;1m")
    # Needed for later, used to avert crashes in event of mischaracterisation
    skip = False

    # Accepts user input
    try : dicenum = int(input(":flushed:, h-hey, w-welcome to Dice Emporium, p-please press 1 or 2 for the desired amount of d-dice uwu: "))
    except : skip = True, print("*Entry of alphabetic characters crashes the program, you are rushed to the local Pokemon Centre*")

    # Defines ASCII artwork for graphical use
    a1 = ("-----\n|   |\n| o |\n|   |\n-----")
    a2 = ("-----\n|o  |\n|   |\n|  o|\n-----")
    a3 = ("-----\n|o  |\n| o |\n|  o|\n-----")
    a4 = ("-----\n|o o|\n|   |\n|o o|\n-----")
    a5 = ("-----\n|o o|\n| o |\n|o o|\n-----")
    a6 = ("-----\n|o o|\n|o o|\n|o o|\n-----")

    # For in case of alphabetic character entry, averts crashes
    if skip == False:
        # User's selection of either 1 or 2 dice decides which function runs
        if dicenum == 1:
            aroll()
        elif dicenum == 2:
            aroll()
            broll()
            # Makes a string of the product of the two values rolled
            aplusb = str(rolla + rollb)
            print("The total value of your roll is " + aplusb)
        else : print("Invalid selection, please make a note of it")

    try: # reversion request
        yn = int(input(white + "Revert program? 1 Yes, 2 No: ")) # Creates yes/no instance
        if yn == 1 : start() # If user selects option 1 the program reverts to start function
        elif yn == 2 : print(yellow + "Shutting down..." + white), exit() # If option 2 was selected, the program terminates
        else : print("Invalid selection, " + yellow + "shutting down..." + white), exit() # If otherwise program is terminated
    except: print("Invalid selection, " + yellow + "shutting down..." + white), exit()

# Starts :PogU:
start()