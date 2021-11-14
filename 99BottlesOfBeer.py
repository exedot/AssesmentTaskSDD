def start():
    # Creates variable to hold value
    n = int(99)
    # Starts For loop, giving max and min value necessary to process
    for n in range(99,-1):
        if n>2:
            # Initiates maximum number of beer to be taken down(99) until reaching 2
            print(str(n) + " bottles of beer on the wall,")
            print(str(n) + " bottles of beer.")
            print("Take one down, pass it around,")
            print(str(n-1) +" bottles of beer on the wall.")
            print("")
        elif n==2:
            # Once reaching 2, an alternate version is constructed to retain grammatical consistency between bottles/bottle
            print(str(n) +" bottles of beer on the wall,")
            print(str(n) +" bottles of beer.")
            print("Take one down, pass it around,")
            print(str(n-1) +" bottle of beer on the wall.")
            print(str(""))
        elif n==1:
            # Same is done here for no. 1
            print(str(n) +" bottle of beer on the wall,")
            print(str(n) +" bottle of beer.")
            print("Take one down, pass it around,")
            print("no more bottles of beer on the wall.")
            print("")
        else:
            # Once value is exhausted, the song draws to a close
            print("no more bottles of beer on the wall,")
            print("no more bottles of beer.")
            print("Go to the strore and buy some more,")
            print("99 bottles of beer on the wall.")
# init prog dude
start()