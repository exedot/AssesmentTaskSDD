def start():
    c = 0 ; f = 0

    blue = str("\u001b[34;1m")
    red = str("\u001b[31;1m")
    white = str("\u001b[37m")
    yellow = str("\u001b[33;1m")

    # State use cases
    print(white + "Press 1 for " + blue + "Celsius" + white + " to " + red + "Farenheit") 
    print(white + "Press 2 for " + red + "Farenheit" + white + " to " + blue + "Celsius")

    moo = int(input(white + "Select mode of operation: ")) # Requests user input

    # Once checked and validatated user selection, requests temperature value
    if moo == 1 : c = int(input("Input" + blue + " Celsius " + white + "temperature value: "))
    elif moo == 2 : f = int(input("Input" + red + " Farenheit " + white + "temperature value: "))
    else: print(white + "Invalid selection, please make a note of it")

    # Conversion equations, Celsius to Farenheit and vice versa
    c2f = ((c * 9/5) + 32) ; f2c = ((f - 32) * 5/9)

    # Converts values from type float to string
    farval = str(c2f)
    celval = str(f2c)

    fs = str(f)
    cs = str(c)

    # Processes value through selected equation, breaking upon completion or detection of invalidity
    while moo != 1 or moo !=2:

        if moo == 1 : print(blue + cs + "°C" + white + " equates to " + red + farval + "°F")
        elif moo == 2 : print(red + fs + "°F" + white + " equates to " + blue + celval + "°C")
        else : print(white + "HAHAHAHAHAHAHAHAHAHA YOU FUUUCKEDDD UPPPP BIATCH, get dunked on virgin")
        break

    # Requests reversion
    yn = int(input(white + "Revert program? 1 yes, 2 no: "))
    if yn == 1 : start() # If user selects option 1 the program reverts to start function
    elif yn == 2 : print(yellow + "Shutting down..." + white), exit() # If option 2 was selected, the program terminates
    else : print("Invalid selection, " + yellow + "shutting down..." + white), exit() # If otherwise program is terminateds

# Starts prog yo
start()


