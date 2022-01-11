from web3 import Web3


def send_transaction(message):
    w3 = Web3(Web3.HTTPProvider(
        'https://ropsten.infura.io/v3/2a3c5c1ec3bd4149bc863f11c5babdd1'))
    address = '0x4dDBeF5971577d827bB7DE043c35Fe98b0A6f708'
    privateKey = '0xb12e533a80b8ba2c0fe0310e6ff0e696665e2927b1c58146ed0731798bfa68c8'
    nonce = w3.eth.get_transaction_count(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.sign_transaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.send_raw_transaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId
