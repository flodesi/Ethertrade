import csv

class update_database:

    def __init__(self, file) -> None:
        self.contracts = []
        self.file = file
        with open(file, 'rt') as rf:
             reader = csv.reader(rf, delimiter=',')
             for row in reader:
                 row[0] = int(row[0])
                 row[3] = float(row[3])
                 row[4] = float(row[4])
                 self.contracts.append(row)
        rf.close()

    def add_tracking(self, contract_id, tracking, carrier):
        for item in self.contracts:
            if item[0] == contract_id:
                item[7] = tracking
                item[8] = carrier
        self.write_csv()

    def change_balance(self, contract_id, amount):
        for item in self.contracts:
            if item[0] == contract_id:
                item[4] = amount
        self.write_csv()

    def change_status(self, contract_id):
        for item in self.contracts:
            if item[0] == contract_id:
                if item[6].equals('Incomplete'):
                    item[6] = 'Complete'
        self.write_csv()

    def get_contracts(self):
        return self.contracts

    def write_csv(self):
        with open('customer_contracts.csv', 'w', newline='') as wf:
            writer = csv.writer(wf)
            writer.writerows(self.contracts)
        wf.close()
