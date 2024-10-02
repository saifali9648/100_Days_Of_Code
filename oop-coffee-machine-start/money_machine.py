class MoneyMachine:

    CURRENCY = "₹"

    COIN_VALUES = {
        "one_rupee": 1,
        "two_rupee": 2,
        "five_rupee": 5,
        "ten_rupee": 10,
        "twenty_rupee":20
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin} chillar/khulla_piasa 🤣😂 ?💰₹: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is your khulla/chillar/change{self.CURRENCY}{change}.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money🤣. Money refunded👉 🙆‍♂️ haaye! ! thode or khulle/chillar daliye.")
            self.money_received = 0
            return False
