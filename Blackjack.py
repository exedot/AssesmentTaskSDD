def start():
    import random
    # Dealer's cards x player's cards
    dc=[]
    pc=[]

    while len(dc) != 2:
        dc.append(random.randint(1, 11))
        if len(dc) == 2:
            print("Dealer has ", dc)