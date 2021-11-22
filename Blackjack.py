class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
colors = ['heart', 'diamonds', 'spades', 'clubs']
deck = [Card(value, color) for value in range(1, 14) for color in colors]
values = ['ace', '2', '3','4', '5','6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
