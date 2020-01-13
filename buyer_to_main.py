from web3 import Web3
# from web3 import *

class transaction_to_main:

    def __init__(self):
        ganache_url = 'http://127.0.0.1:7545'
        web3 = Web3(Web3.HTTPProvider(ganache_url))
        self.account = "0xcFc5d2c89E76c6B992b85f76fA5c9045ebBDb9af"

        self.nonce = web3.eth.getTransactionCount(self.account)

    def send(self, amount, wallet, private_pass):
        ganache_url = 'http://127.0.0.1:7545'
        web3 = Web3(Web3.HTTPProvider(ganache_url))

        print(web3.isConnected())

        account_2 = "0xcFc5d2c89E76c6B992b85f76fA5c9045ebBDb9af"
        account_1 = wallet

        nonce = web3.eth.getTransactionCount(account_1)

        tx = {
            'nonce': nonce,
            'to': account_2,
            'value': web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei')
            }

        signed_tx = web3.eth.account.signTransaction(tx, private_pass)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
