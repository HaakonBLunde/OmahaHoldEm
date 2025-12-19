import cardsAndDeck

#mydeck = cardsAndDeck.Deck(shuffle=True)

#pre-flop, flop, turn, river

# hand ranking
# royal flush,
# straight flush,
# quads,
# house,
# flush,
# straight,
# trips,
# two pair,
# pair,
# highcard

# a player has a hand consisting of cards and a stack, for every round of play the player might
#check, call or raise the bet. checking is available when there is no bet and first becomes an
#available action after the flop. raising is always available given that there is more money in
#the stack. calling is effectively always available as checking could be considered a special
# type of calling. in computer terms they are the same as calling matches your bet to the current bet
# and whenever checking is possible the current bet is 0



class Player:
    #maybe later I make hand a different class
    def __init__(self,seating_number, initial_stack=150):
        #a player has a hand and a stack
        #initial stack is a magic number based on anecdote
        self.stack = initial_stack
        self.name = seating_number
        self.staked_this_round = 0
        self.staked_this_game = 0
        self.hand = []
        self.alive = True

    def resetPlayer(self):
        #reset the player to play a new hand
        self.hand = []
        self.alive = True
        self.staked_this_round = 0
        self.staked_this_game = 0

    def resetStake(self):
        #players need to track how much they have staked in order to bid or call bids
        #stakes reset whenever a card is dealt, this method has to be invoked for all
        #players whenever a card is dealt.
        self.staked_this_game += self.staked_this_round
        self.staked_this_round = 0

    def draw(self, card):
        #i do not think players draw, might remove later
        self.hand.append(card)

    def getHand(self):
        return self.hand

    def raiseBet(self, amount_to_raise, current_bet):
        #takes current bet and amount to raise, returns new bet
        #to raise you first match the existing bet, then provide an additional bet
        sum_to_raise = current_bet + amount_to_raise - self.staked_this_round
        self.stack -= sum_to_raise
        self.staked_this_round = amount_to_raise + current_bet

        return self.staked_this_round

    def call(self, current_bet):
        #calling consists of betting (current_bet-self.stake)
        #checking and calling are the same thing except for the first speaker
        sum_to_call = current_bet - self.staked_this_round
        self.staked_this_round = current_bet
        self.stack -= sum_to_call

    def fold(self):
        #player folds and can not do any actions.
        self.alive = False

    def showdown(self):
        #the showing of the cards in the hand at the end of the hand
        #redundant, consider removing. getHand() is better in terms of naming
        return self.hand

    def check(self):
        #return 0 ?? will figure it out later
        return 0

    def pay_small(self, small_blind=2):
        #move small_blind to some other place later maybe
        #as paying blinds happen at the start of the game it should be fine to just set the
        #staked amount to be equal to the blinds
        self.staked_this_round = small_blind
        self.staked_this_game = small_blind
        self.stack -= small_blind

    def pay_big(self, big_blind=4):
        #same comments as for pay_small, only for big blinds
        self.staked_this_round = big_blind
        self.staked_this_game = big_blind
        self.stack -= big_blind

    def pay_ante(self, ante=5):
        #not the same as big or small as this a pure tax and doesn't count as a bet.
        self.stack -= ante


class OmahaHoldEm:
    def __init__(self, player_count=8, small_blind=2, big_blind=4, ante=5, buy_in=150):
        #these are the usual parameters players of omaha agree on before playing
        #all values are sampled from anecdotal experience
        self.player_count = player_count
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.ante = ante
        #now we need a deck of cards to play with
        self.deck = cardsAndDeck.Deck()
        #you can never shuffle your deck too much
        self.deck.shuffle()
        #we need players

#fra 5 velg tre, fra 4 velg 2
# 0 og (1,2,3)
# 1 og (2,3)
# 2 og 3
# 6 til sammen + 1 for hele hånden for anti-cheat er det bare å lage 6 hashes som
# sendes etter hånden er delt og i showdown sjekkes vinnerkombo mot eksisterende hashes.
# for å fullstending desentralisere spillet må alle spillere sitte på alle hashes