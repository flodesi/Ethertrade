import update_database
import user_db_access as access
import validate

class data_handling:

    def __init__(self):
        self.ls_of_users = access.user_database('login.csv')
        self.ls_of_contracts = []
        self.contracts = update_database.update_database('customer_contracts.csv').get_contracts()
        for item in self.contracts:
            buyer_wallet = self.ls_of_users.get_user_wallet(item[1])
            buyer_pass = self.ls_of_users.get_user_wallet_pass(item[1])
            seller_wallet = self.ls_of_users.get_user_wallet(item[2])
            self.ls_of_contracts.append(validate.validate(buyer_wallet, buyer_pass, seller_wallet, item[3], item[0]))

    def add_funds_to_contract(self, contract_id, amount):
        for item in self.ls_of_contracts:
            if item.get_id() == int(contract_id):
                item.pay(amount)
                amount_owing = item.view_amount_owing()
                self.contracts.change_balance(int(contract_id), amount_owing)

    def add_tracking(self, contract_id, tracking_num, carrier):
        for item in self.ls_of_contracts:
            if item.get_id() == contract_id:
                complete = item.attempt_complete(tracking_num, carrier)
                if complete:
                    self.contracts.add_tracking(contract_id, tracking_num, carrier)
                    self.contracts.change_status(contract_id)
