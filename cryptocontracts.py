import buyer_to_main as buyer
import main_to_seller as seller

class cryptocontracts:

    filled = False
    wallet = "this is the company wallet address"

    def __init__(self, buy_wallet, buy_pass, sell_wallet, amount) -> None:
        self.amount = amount
        self.balance = amount
        self.buyer_wallet = buy_wallet
        self.buy_pass = buy_pass
        self.sell_wallet = sell_wallet
        self.transaction_to_main = buyer.transaction_to_main()
        self.main_to_seller = seller.main_to_seller()

    def add_funds(self, amount) -> None:
        self.balance = float(self.balance)
        amount = float(amount)
        if amount <= self.balance:
            self.balance -= amount
            self.send_amount(amount, self.buyer_wallet, self.buy_pass)
            if self.balance == 0:
                self.fill_contract()
        else:
            amount_to_return = amount - self.balance
            self.balance = 0
            self.send_amount(self.balance, self.buyer_wallet, self.buy_pass)
            self.fill_contract()

    def is_filled(self) -> bool:
        return self.filled

    def get_balance(self) -> float:
        return self.balance

    def send_amount(self, amount, wallet, private_key) -> None:
        self.transaction_to_main.send(amount, wallet, private_key)

    def fill_contract(self):
        self.main_to_seller.send(self.amount, self.sell_wallet)
