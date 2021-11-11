def start():
    n = int(99)
    for n in range(99,-1,-1):
        if n>2:
            print(str(n) + " bottles of beer on the wall,")
            print(str(n) + " bottles of beer.")
            print("Take one down, pass it around,")
            print(str(n-1) +" bottles of beer on the wall.")
            print("")
        elif n==2:
            print(str(n) +" bottles of beer on the wall,")
            print(str(n) +" bottles of beer.")
            print("Take one down, pass it around,")
            print(str(n-1) +" bottle of beer on the wall.")
            print(str(""))
        elif n==1:
            print(str(n) +" bottle of beer on the wall,")
            print(str(n) +" bottle of beer.")
            print("Take one down, pass it around,")
            print("No more bottles of beer on the wall.")
            print("")
        else:
            print("No more bottles of beer on the wall,")
            print("no more bottles of beer.")
            print("Go to the strore and buy some more,")
            print("99 bottles of beer on the wall.")
start()