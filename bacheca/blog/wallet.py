from web3 import Web3

w3 = Web3(Web3.HTTPProvider(
    'https://ropsten.infura.io/v3/2a3c5c1ec3bd4149bc863f11c5babdd1'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f"Your address: {address}\n Your Key:{privateKey}")
