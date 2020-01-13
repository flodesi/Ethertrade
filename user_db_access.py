import csv

class user_database:

    def __init__(self, file) -> None:
        self.users = []
        self.file = file
        self.contracts = []
        with open(file, 'rt') as rf:
            reader = csv.reader(rf, delimiter=',')
            for row in reader:
                self.users.append(row)
        rf.close()
        with open('customer_contracts.csv', 'rt') as rf:
            reader = csv.reader(rf, delimiter=',')
            for row in reader:
                row[0] = int(row[0])
                row[3] = float(row[3])
                row[4] = float(row[4])
                self.contracts.append(row)
        rf.close()

    def get_user_wallet(self, username):
        for item in self.users:
            if item[0] == username:
                return item[2]

    def get_user_wallet_pass(self, username):
        for item in self.users:
            if item[0] == username:
                return item[3]
