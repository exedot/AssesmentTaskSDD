def start():
    beer = int(99)
    bs = str(beer)
    b = str(bs + " bottles of beer on the wall,\n" + bs + " bottles of beer.\nTake one down, pass it around\n" + bs + " bottles of beer on the wall")
    while beer >=1: hasbeer = True

    while hasbeer == True:
        print(b)
        beer = (beer - 1); return beer
    
    if hasbeer == False:
        print("No more bottles of beer on the wall,\nno more bottles of beer.\nGo to the store and buy some more,\n99 bottles of beer on the wall...")

start()