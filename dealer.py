#import deck and card player here


from card_player import Card_player
from deck import Deck



class Dealer(Card_player,Deck):

    def __init__(self):
        self.card_player = Card_player()
        self.deck = Deck()
    

    def draw_card(self):
        self.deck.generate_deck()
        card = self.deck.take_card()

        self.card_player.set_name = "Dealer"
        #self.card_player.set_hand(card)
        self.card_player.get_hand()

        

        

        
        



    '''
    def sayhi(self):
        
        print("ayoooo")
        print(f"Name is: {self.name}")

    def changeName(self,newName):
        self.name = newName
    '''