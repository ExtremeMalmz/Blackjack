import random
from card import Card

class Deck():
    def __init__(self):
        print("Deck")

        self.cards = []


    def generate_deck(self):
        print("creates a deck")

        #cardDeck = Card(52)

        
        for i in range(52):
            self.cards.append(Card(i))

        #print(self.cards[51])

        
        
        '''
        deck = []

        for i in range(52):
            #deck.append(self.cards(i))
            print(cardDeck[i])
        '''
        return self.cards

    def shuffle_deck(self):
        print("shuffles the deck so you dont get the same card twice")
        # Shuffle the cards (don't forget to include the random module):
        random.shuffle(self.cards)
        #print(self.cards[51])

    def take_card(self):
        #print("take a card any card and return it")
        randomCard = random.choice(self.cards)
        return randomCard