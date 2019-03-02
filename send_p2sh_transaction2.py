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
from bitcoinutils.keys import P2pkhAddress, P2shAddress, PrivateKey
from bitcoinutils.script import Script


def main():
    # always remember to setup the network
    setup('testnet')

    #
    # This script creates a P2SH address containing a P2PK script and sends
    # some funds to it
    #

    #
    # create transaction output using P2SH scriptPubKey (locking script)
    # (the recipient will give us the final address  but for now we create it
    # for demonstration purposes)
    #

    # secret key corresponding to the pubkey needed for the P2SH (P2PK) transaction
    p2pk_sk = PrivateKey('cRvyLwCPLU88jsyj94L7iJjQX5C2f8koG4G2gevN4BeSGcEvfKe9')
    p2pk_pk = p2pk_sk.get_public_key().to_hex()
    redeem_script = Script([p2pk_pk, 'OP_CHECKSIG'])
 	
	#TESTE_SUZANA
    addressObj = P2shAddress.from_script(redeem_script)
    print("addressObj=" + addressObj.to_address())
	#TESTE_SUZANA	
	

	# you can initially spend a specific UTXO that you know (e.g. with the txid after you send some funds to the address).  Then if everything works you can use the address to find all tx in that address and spend them. Make sure the timelock works and that you can spend the funds as expected.
	
	
	# The 2nd program should display the raw signed transaction that is to be sent to a bitcoin node plus _send_ the transaction to a node. The last part is not possible with the bitcoin-utils library since I have not impl. a node proxy yet. So you have to use another lib or finish with the cli commands (commented out of course) that I have to run in order to send the raw tx to a bitcoin node.
	# The P2SH addr could be recalculated in 2nd program since we have the redeem script! Providing the P2SH addr saves you from this small calculation and 'connects' the 2 programs :-)

	# Re fees, I would rather you calculate the 'appropriate' fee and explain in comments how/why you did it this way. Ideally, you would consult an online service to get an estimate of the appropriate fee. This is minor for assignment purposes but major for production systems.
	
	#https://bitcoin.stackexchange.com/questions/83650/how-does-nsequence-check-sequence-verify-work
    #The 2nd program requires a private key as well... that is what unlock the funds.
	
	
	
	##### NAO PRECISA PARA O ASSIGNMENT DAQUI EM DIANTE #######
	
	
    # create transaction input from tx id of UTXO (contained 0.1 tBTC)
    txin = TxInput('76464c2b9e2af4d63ef38a77964b3b77e629dddefc5cb9eb1a3645b1608b790f', 0)

    # address we are spending from
    from_addr = P2pkhAddress('n4bkvTyU1dVdzsrhWBqBw8fEMbHjJvtmJR')

    # secret key of address that we are trying to spent
    sk = PrivateKey('cTALNpTpRbbxTCJ2A5Vq88UxT44w1PE2cYqiB3n4hRvzyCev1Wwo')

	#SUZANA ---- ASSINA COM P2SH do SCRIPT
    txout = TxOutput( 0.09, redeem_script.to_p2sh_script_pub_key() )

	
	
    # no change address - the remaining 0.01 tBTC will go to miners)

    # create transaction from inputs/outputs -- default locktime is used
    tx = Transaction([txin], [txout])

    # print raw transaction
    print("\nRaw unsigned transaction:\n" + tx.serialize())

    # use the private key corresponding to the address that contains the
    # UTXO we are trying to spend to create the signature for the txin
    sig = sk.sign_input(tx, 0, from_addr.to_script_pub_key() )
    #print(sig)

    # get public key as hex
    pk = sk.get_public_key()
    pk = pk.to_hex()
    #print (pk)

    # set the scriptSig (unlocking script)
    txin.script_sig = Script([sig, pk])
    signed_tx = tx.serialize()

    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + signed_tx)
    print("\nTxId:", tx.get_txid())


if __name__ == "__main__":
    main()
