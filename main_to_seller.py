from web3 import Web3

class main_to_seller:

    def __init__(self):
        ganache_url = 'http://127.0.0.1:7545'
        web3 = Web3(Web3.HTTPProvider(ganache_url))
        print(web3.isConnected())
        self.account = '0xcFc5d2c89E76c6B992b85f76fA5c9045ebBDb9af'
        self.private_key = '57c81502a0fc125f5f969f9f8062265de1e0874705686d7ef18b5f3c21a9f6dc'

        self.nonce = web3.eth.getTransactionCount(self.account)

    def send(self, amount, wallet):
        ganache_url = 'http://127.0.0.1:7545'
        web3 = Web3(Web3.HTTPProvider(ganache_url))

        print(web3.isConnected())

        account_2 = '0xcFc5d2c89E76c6B992b85f76fA5c9045ebBDb9af'
        account_1 = wallet

        nonce = web3.eth.getTransactionCount(account_2)


        tx = {
            'nonce': self.nonce,
            'to': wallet,
            'value': web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
            }

        signed_tx = web3.eth.account.signTransaction(tx, self.private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
