import random
from itertools import count

suits = ["hearts", "clubs", "spades", "diamonds"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card:
#cards have suits and values, aces have values 1 and 14
#jokers might exist later. They could have suit and value set to joker and gamelogic can handle it.
# idk any games with jokers in them
#in blackjack aces are 1 and 11 and picture cards are 10
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.valName = str(value)
        #self.blackJackVal = value
        match value:
            case 1:
                self.valName = "Ace"
            case 11:
                self.valName = "Jack"
            case 12:
                self.valName = "Queen"
            case 13:
                self.valName = "King"

    def getValue(self):
        #as the value of the ace depends on the game we just give the value
        #when using this project be mindful to properly define what happens with the ace
        #if self.value == 1:
            #i think?
            #no i don't think so. aces being 14 depends on the game and should be handled by game logic
        #    return (1, 14)

        return self.value

    def getSuit(self):
        return self.suit

    def getName(self):
        name = self.valName + " of " + str(self.suit)
        return name

    def __str__(self):
        return self.getName()

class Deck:
    # a deck has 52 cards by default
    # todo add decks of different sizes for shortdeck(6-Ace). Just make an alternative list of values
    #  blackjack(uneven decks of some random size). Something to do with normal distributions. also jokers i
    #  guess, but i don't know any games with jokers
    def __init__(self, jokers=False, shuffle=False):
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))
        if shuffle:
            random.shuffle(self.deck)

    def getDeck(self):
        return self.deck

    def printDeck(self):
        for card in self.deck:
            print(card.getName())

    def countCards(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        card = self.deck.pop()
        return card

    def reset(self):
        #needs to account for jokers if they come into play
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

        random.shuffle(self.deck)
