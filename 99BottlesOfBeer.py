def start():
    # Creates variable to hold value
    bottles = int(99)
    # Starts For loop, giving max and min value necessary to process
    for bottles in range(99,-1, -1):
        if bottles>2:
            # Initiates maximum number of beer to be taken down(99) until reaching 2
            print(str(bottles) + " bottles of beer on the wall,")
            print(str(bottles) + " bottles of beer.")
            print("Take one down, pass it around,")
            print(str(bottles-1) +" bottles of beer on the wall.")
            print("")
        elif bottles==2:
            # Once reaching 2, an alternate version is constructed to retain grammatical consistency between bottles/bottle
            print(str(bottles) +" bottles of beer on the wall,")
            print(str(bottles) +" bottles of beer.")
            print("Take one down, pass it around,")
            print(str(bottles-1) +" bottle of beer on the wall.")
            print(str(""))
        elif bottles==1:
            # Same is done here for no. 1
            print(str(bottles) +" bottle of beer on the wall,")
            print(str(bottles) +" bottle of beer.")
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