from ic.agent import *
from ic.identity import *
from ic.client import *
from ic.candid import Types, encode
from ic.canister import Canister
from utils.fileio import FileIO
import requests
from pathlib import Path
from pem import identity

# nft metadata, owners, listings, soldlistings
class NFTUtils:
    def __init__(self, standard, canisterId):
        self.canisterId = canisterId
        self.standard = standard
        candid = self.getCandid(standard)
        self.identity = identity
        client = Client()
        agent = Agent(identity, client)
        self.canister = Canister(agent=agent, canister_id=canisterId, candid=candid)

    def getCandid(self, version):
        switcher={
            'ext': open("candid/ext_nft.did").read(),
        }
        return switcher.get(version, '')

    def recover(self, fromAddress, toAddress, tokenId, subAccount):
        params = {
                    'from': { 'address' : fromAddress}, 
                    'to': { 'address' : toAddress}, 
                    'token': tokenId, 
                    'amount': 1, 
                    'memo' : [],
                    'notify' : False,
                    'subaccount' : [subAccount],
                    }
        result = self.canister.transfer(params)
        print(result)

