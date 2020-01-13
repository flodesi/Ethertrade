import tracker
import cryptocontracts

class validate:

    def __init__(self, buy_wallet, buy_pass, sell_wallet, amount, contract_id) -> None:
        self.tracker = tracker.tracker()
        self.cryptocontracts = cryptocontracts.cryptocontracts(buy_wallet, buy_pass, sell_wallet, amount)
        self.is_complete = False
        self.contract_id = contract_id

    def pay(self, amount) -> None:
        self.cryptocontracts.add_funds(amount)

    def get_id(self) -> int:
        return self.contract_id

    def view_amount_owing(self) -> float:
        return self.cryptocontracts.get_balance()

    def view_tracking_number(self) -> str:
        return self.tracker.get_tracking_number()

    def is_complete(self) -> bool:
        return self.is_complete

    def attempt_complete(self, tracking_num, carrier) -> bool:
        self.tracker.set_tracking_number(tracking_num)
        self.tracker.set_carrier(carrier)
        if self.tracker.is_valid() and self.cryptocontracts.is_filled:
            self.cryptocontracts.fill_contract()
            self.is_complete = True
            return True
        else:
            return False
