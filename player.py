class Player():
    def __init__(self,balance: int):
        print("Player Initialised")

        self.balance = balance

    def get_balance(self):
        #print("Gets the balance of the player")
        return self.balance

    def add_money(self, moneyWon):
        print("adds money to balance when theres a win")

        self.balance = self.balance + moneyWon
        return self.balance

    def remove_money(self, moneyLost):
        print("removes money when the player loses")

        self.balance = self.balance - moneyLost
        #gotta check if its at or below ZERO somewhere
        return self.balance