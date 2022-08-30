from dealer import Dealer
from player import Player
from deck import Deck

class Blackjack():
    #the main of the game
    def __init__(self):
        print("Initialiser")

        self.dealer = Dealer()
        self.player = Player(0)
        self.deck = Deck()


        
        #Blackjack.play(self)

    def welcome(self):
        #print("Welcome screen thats it")

        print("="*40)
        print("Välkommen till Black Jack!")
        print("="*40)

    def play(self):
        #print("Starts the game")

        '''
        
        playerName = input("Vad heter du? ")
        amountOfCash = input("Hur mycket vill du spela för? ")
        dealerName = input("Vad heter dealerna idag? ")
        dealerName = "-" + dealerName
        print(f"Välkommen {playerName} och lycka till!")
        print(f"{dealerName} är dealer idag")
        print("="*40)
        '''

        playerName = "Tuvin"
        amountOfcash = 100
        dealerName = "-X"


        self.player = Player(amountOfcash)

        #While loop starts here
        while(True):
            yesOrNo = input("Vill du spela? (y/n) ")

            if yesOrNo == "y":
                #amountOfCash should be checked with the player
                amountOfcash = self.player.get_balance()

                print("*"*40)
                Blackjack.status(self,playerName,amountOfcash)
                print("*"*40)

                '''
                amountOfcash = self.player.add_money(20)
                print(amountOfcash)
                amountOfcash = self.player.remove_money(21)
                print(amountOfcash)
                '''

                amountGamblingOn = input("Hur mycket vill du satsa?")

                Blackjack.dealer_draw_cards(self)

            else:
                print(f"{playerName} vann {amountOfcash}\nTack för att du spelade")
                exit()
            
    def status(self,playerName,amountOfcash):
        #print("Printar status på spelet")
        print(f"Namn: {playerName}, Pengar: {amountOfcash}")
        

    def dealer_draw_cards(self):
        #print("Dealer is gonna draw some cards here for both the house and player")

        #player cards are printed out in hand while the house is printed in dealer
        
        
        self.dealer.draw_card()
        


        '''
        #this aint supposed to be here
        playerCards = []
        
        self.deck.generate_deck()

        for i in range(2):
            randomCard = self.deck.take_card()
            playerCards.append(randomCard)
        
        print(playerCards[0])
        print(playerCards[1])
        '''
