# Copyright (C) 2018 The python-bitcoin-utils developers
#
# This file is part of python-bitcoin-utils
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoin-utils, including this file, may be copied,
# modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from bitcoinutils.setup import setup
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, PrivateKey
from bitcoinutils.script import Script


def main():
    # always remember to setup the network
    setup('testnet')

    # create transaction input from tx id of UTXO (contained 0.4 tBTC)
    txin = TxInput('41c0c1b9aff5d2608a00dd458120b86b38b26a19bb80a4085e0e868e4be0941a', 0)
	
    # create transaction output using P2PKH scriptPubKey (locking scrip
    addr = P2pkhAddress('2NCpHygg5xJ4FJr3p8gpEzyZtX6R8JxNbZF')
#    txout = TxOutput( 0.010, Script(['OP_DUP', 'OP_HASH160', addr.to_hash160(),'OP_EQUALVERIFY', 'OP_CHECKSIG']) )

    # create another output to get the change - remaining 0.01 is tx fees
    # note that this time we used to_script_pub_key() to create the P2PKH
    # script
#    change_addr = P2pkhAddress('2NAeLEJfh6rpQ37diquGQr7CcBGTwCEyEte')
#   change_txout = TxOutput(0.113, change_addr.to_script_pub_key())


  

if __name__ == "__main__":
    main()
	
	