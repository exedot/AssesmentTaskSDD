pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 
guesses = ''
turns = 7
word = "kilimanjaro"

while turns > 0:        
    failed = 0             
    for char in word:    
        if char in guesses:    
            print (char, ) 
        else:
            print ("_", )
            failed += 1    
    if failed == 0:        
        print  ("You won")
        break
    guess = input("guess: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print ("Wrong")
        print ("You have", + turns, 'more guesses' )
        if turns == 0:           
            print ("You Lose")