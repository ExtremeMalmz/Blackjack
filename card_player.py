from hand import Hand

class Card_player():
    def __init__(self):
        self.hand = Hand()

    def get_name(self):
        print("Gets a name")
        return self.name

    def set_name(self):
        print("sets a name")
        self.name = self.name 

    def get_hand(self):
        print("Gets a hand based on name")
        return 0

    def set_hand(self, Hand):
        print("sets the hand")
        return Hand

        