from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))


account_1 = '0xcFc5d2c89E76c6B992b85f76fA5c9045ebBDb9af'
account_2 = '0x9b9E55d0b1e06f837206BBC548430E6D361Af11B'

private_key = '57c81502a0fc125f5f969f9f8062265de1e0874705686d7ef18b5f3c21a9f6dc'

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
    }

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
