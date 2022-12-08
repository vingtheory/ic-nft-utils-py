from ic.agent import *
from ic.identity import *
from ic.client import *
from ic.candid import Types, encode
from ic.canister import Canister
from utils.fileio import FileIO

# nft metadata, owners, listings, soldlistings
class CCCNFTCanisterUtils:
    def __init__(self, inputCollectionName, inputSrcNftCanisterId, inputtotalTokensSuppy):
        self.collectionName = inputCollectionName
        self.totalTokensSupply = inputtotalTokensSuppy
        candid = open("candid/ccc_nft.did").read()
        identity = Identity()
        client = Client()
        agent = Agent(identity, client)
        self.canister = Canister(agent=agent, canister_id=inputSrcNftCanisterId, candid=candid)

    def downloadAllTokensMetadata(self):
        tokenIndex = 0
        tokenDetails = []
        while tokenIndex < self.totalTokensSupply:
             res = self.canister.getTokenById(tokenIndex + 1)
             tokenDetails.append(res)
             tokenIndex = tokenIndex + 1
        FileIO.writeToJSON('tokensMetadata', tokenDetails)

    def uploadAllTokensMetadata(self):
        tokensMetadata = FileIO.readFromJSON('tokensMetadata')
        print(tokensMetadata)

    def downloadAllComponentsInfo(self):
        componentSize = self.canister.getComponentsSize()
        componentsDetails = []
        index = 0
        while index < componentSize[0]:
             res = self.canister.getComponentById(index)
             componentsDetails.append(res)
             index = index + 1
        FileIO.writeToJSON('componentsDetails', componentsDetails)

    def uploadAllComponentsInfo(self):
        componentsDetails = FileIO.readFromJSON('componentsDetails')
        print(componentsDetails)

    def downloadAllListings(self):
        listings = self.canister.getListings()
        FileIO.writeToPickle('listings', listings[0])

    def uploadAllListings(self):
        listings = FileIO.readFromPickle('listings')

    def downloadAllSoldListings(self):
        soldListings = self.canister.getSoldListings()
        FileIO.writeToPickle('soldListings', soldListings[0])

    def uploadAllSoldListings(self):
        soldListings = FileIO.readFromPickle('soldListings')

    def downloadAllTokenAndOwnerMetadata(self):
        tokenIndex = 0
        owners = []
        while tokenIndex < self.totalTokensSupply:
             mintNumber = tokenIndex + 1 
             res = self.canister.ownerOf(mintNumber)
             owners.append({'mintNumber': mintNumber, 'owner': res[0][0].to_str()})
             tokenIndex = tokenIndex + 1
        FileIO.writeToJSON('owners', owners)

    def uploadAllTokenAndOwnerMetadata(self):
        owners = FileIO.readFromJSON('owners')
        print(owners)

# image
class CCCNFTMetadataCanisterUtils:
    def __init__(self, inputCollectionName, inputSrcMetadataCanisterId, inputtotalTokensSuppy):
        self.collectionName = inputCollectionName
        self.totalTokensSupply = inputtotalTokensSuppy
        candid = open("candid/ccc_nft_metadata.did").read()
        identity = Identity()
        client = Client()
        agent = Agent(identity, client)
        self.canister = Canister(agent=agent, canister_id=inputSrcMetadataCanisterId, candid=candid)

    def downloadAllImages(self):
        tokenIndex = 0
        images = []
        while tokenIndex < self.totalTokensSupply:
             mintNumber = tokenIndex + 1 
             httpRequest = { 'body' : [], 'headers': [], 'method' : 'get', 'url':f"token/{mintNumber}"}
             res = self.canister.http_request(httpRequest)
             images.append({'mintNumber': mintNumber, 'image': res[0]})
             tokenIndex = tokenIndex + 1
        FileIO.writeToPickle('images', images)

    def uploadAllImages(self):
        images = FileIO.readFromPickle('images')
        print(images)

# transactions
class CCCNFTStorageCanisterUtils:
    def __init__(self, inputCollectionName, inputSrcStorageCanisterId, inputtotalTokensSuppy):
        self.collectionName = inputCollectionName
        self.totalTokensSupply = inputtotalTokensSuppy
        candid = open("candid/ccc_storage.did").read()
        identity = Identity()
        client = Client()
        agent = Agent(identity, client)
        self.canister = Canister(agent=agent, canister_id=inputSrcStorageCanisterId, candid=candid)

    def downloadAllTransactions(self):
        tokenIndex = 0
        history = []
        while tokenIndex < self.totalTokensSupply:
             mintNumber = tokenIndex + 1 
             res = self.canister.getHistory(mintNumber)
             history.append({'mintNumber': mintNumber, 'history': res[0]})
             tokenIndex = tokenIndex + 1
        FileIO.writeToPickle('history', history)

    def uploadAllTransactions(self):
        history = FileIO.readFromPickle('history')
        print(history)
