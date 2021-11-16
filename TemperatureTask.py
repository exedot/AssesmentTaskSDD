def start():

    # Initialises temporary values to "c" and "f"
    c = float(0) ; f = float(0)
    skip = False ; skip2 = False

    # Assigns colour attributes to appropriate variable
    blue = str("\u001b[34;1m")
    red = str("\u001b[31;1m")
    white = str("\u001b[37m")
    yellow = str("\u001b[33;1m")

    # States use cases
    print(white + "Press 1 for " + blue + "Celsius" + white + " to " + red + "Farenheit") 
    print(white + "Press 2 for " + red + "Farenheit" + white + " to " + blue + "Celsius")

     # Requests user input
    try : moo = float(input(white + "Select mode of operation: ")) 
    except : skip = True, print("*Entry of alphabetic characters crashes the program, you are rushed to the local Pokemon Centre*")
    
    if skip == False:

        # Once checked and validatated user selection, requests temperature value
        try:
            if moo == 1 : c = float(input("Input" + blue + " Celsius " + white + "temperature value: "))
            elif moo == 2 : f = float(input("Input" + red + " Farenheit " + white + "temperature value: "))
            else : print(white + "Invalid selection, please make a note of it")
        except: skip2 = True, print("*Entry of alphabetic characters crashes the program, you are rushed to the local Pokemon Centre*")

        if skip2 == False:
            # Conversion equations, Celsius to Farenheit and vice versa
            c2f = ((c * 9/5) + 32) ; f2c = ((f - 32) * 5/9)
            # Converts values from type float to string
            farval = str(c2f) ; celval = str(f2c)
            # Converts original values
            fs = str(f) ; cs = str(c)
            # Processes value through selected equation, breaking upon completion or detection of invalidity
            while moo != 1 or moo !=2:
                if moo == 1 : print(blue + cs + "°C" + white + " equates to " + red + farval + "°F") # Strings patchwork phrase
                elif moo == 2 : print(red + fs + "°F" + white + " equates to " + blue + celval + "°C")
                else : print(white + "HAHAHAHAHAHAHAHAHAHA YOU FUUUCKEDDD UPPPP BIATCH, get dunked on virgin")
                break

    # Requests reversion
    yn = int(input(white + "Revert program? 1 Yes, 2 No: "))
    if yn == 1 : start() # If user selects option 1 the program reverts to start function
    elif yn == 2 : print(yellow + "Shutting down..." + white), exit() # If option 2 was selected, the program terminates
    else : print("Invalid selection, " + yellow + "shutting down..." + white), exit() # If otherwise program is terminated
# Starts prog yo
start()