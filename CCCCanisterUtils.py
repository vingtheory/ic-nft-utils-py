from ic.agent import *
from ic.identity import *
from ic.client import *
from ic.candid import Types, encode
from ic.canister import Canister
from utils.fileio import FileIO

# nft metadata, owners, listings, soldlistings
class CCCNFTCanisterUtils:
    def __init__(self, inputCollectionName, inputSrcNftCanisterId, inputtotalTokensSuppy, version):
        self.collectionName = inputCollectionName
        self.totalTokensSupply = inputtotalTokensSuppy
        candid = self.getCandid(version)
        identity = Identity()
        client = Client()
        agent = Agent(identity, client)
        self.canister = Canister(agent=agent, canister_id=inputSrcNftCanisterId, candid=candid)

    def getCandid(self, version):
        switcher={
            'v1': open("candid/ccc_nft_v1.did").read(),
            'v2': open("candid/ccc_nft_v2.did").read(),
        }
        return switcher.get(version, '')

    def downloadAllTokensMetadata(self):
        print('Starting - downloadAllTokensMetadata...')
        tokenIndex = 0
        tokenDetails = []
        iterationSuccess = 0
        while tokenIndex < self.totalTokensSupply:
            try:
                # print('tokenIndex: ', tokenIndex)
                res = self.canister.getTokenById(tokenIndex)
                iterationSuccess = 1
            except KeyboardInterrupt: 
                print('User Keyboard Interrupt occured - downloadAllTokensMetadata. Will exit.')
                return
            except:
                print('Exception occured - downloadAllTokensMetadata. Will continue and try again.')
                continue
            finally:
                if (iterationSuccess == 1):
                    tokenDetails.append(res)
                    tokenIndex = tokenIndex + 1
                    iterationSuccess = 0
        FileIO.writeToJSON('tokensMetadata', tokenDetails)
        print('Successful - downloadAllTokensMetadata.')

    def uploadAllTokensMetadata(self):
        tokensMetadata = FileIO.readFromJSON('tokensMetadata')
        print(tokensMetadata)

    def downloadAllComponentsInfo(self):
        print('Starting - downloadAllComponentsInfo...')
        componentSize = self.canister.getComponentsSize()
        componentsDetails = []
        tokenIndex = 0
        while tokenIndex < componentSize[0]:
            try:
                # print('tokenIndex: ', tokenIndex)
                res = self.canister.getComponentById(tokenIndex)
                iterationSuccess = 1
            except KeyboardInterrupt: 
                print('User Keyboard Interrupt occured - downloadAllComponentsInfo. Will exit.')
                return
            except:
                print('Exception occured - downloadAllComponentsInfo. Will continue and try again.')
                continue
            finally:
                if (iterationSuccess == 1):
                    componentsDetails.append(res)
                    tokenIndex = tokenIndex + 1
                    iterationSuccess = 0
        FileIO.writeToJSON('componentsDetails', componentsDetails)
        print('Successful - downloadAllComponentsInfo.')

    def uploadAllComponentsInfo(self):
        componentsDetails = FileIO.readFromJSON('componentsDetails')
        print(componentsDetails)

    def downloadAllListings(self):
        print('Starting - downloadAllListings...')
        listings = self.canister.getListings()
        FileIO.writeToPickle('listings', listings[0])
        print('Successful - downloadAllListings.')

    def uploadAllListings(self):
        listings = FileIO.readFromPickle('listings')

    def downloadAllSoldListings(self):
        print('Starting - downloadAllSoldListings...')
        soldListings = self.canister.getSoldListings()
        FileIO.writeToPickle('soldListings', soldListings[0])
        print('Successful - downloadAllSoldListings.')

    def downloadImageReferenceData(self):
        print('Starting - downloadImageReferenceData...')
        allNftLinkInfo = self.canister.getAllNftLinkInfo()
        FileIO.writeToPickle('allNftLinkInfo', allNftLinkInfo[0])
        print('Successful - downloadImageReferenceData.')

    def uploadAllSoldListings(self):
        soldListings = FileIO.readFromPickle('soldListings')

    # iterate through all nfts index and download one by one - time consuming. use getRegistry instead
    def downloadAllTokenAndOwnerMetadata(self):
        print('Starting - downloadAllTokenAndOwnerMetadata...')
        tokenIndex = 0
        owners = []
        iterationSuccess = 0
        while tokenIndex < self.totalTokensSupply:
            try:
                # print('tokenIndex: ', tokenIndex)
                res = self.canister.ownerOf(tokenIndex)
                iterationSuccess = 1
            except KeyboardInterrupt: 
                print('User Keyboard Interrupt occured - downloadAllTokenAndOwnerMetadata. Will exit.')
                return
            except:
                print('Exception occured - downloadAllTokenAndOwnerMetadata. Will continue and try again.')
                continue
            finally:
                if (iterationSuccess == 1):
                    owners.append({'tokenIndex': tokenIndex, 'owner': res[0][0].to_str()})
                    tokenIndex = tokenIndex + 1
                    iterationSuccess = 0
        FileIO.writeToJSON('owners', owners)
        print('Successful - downloadAllTokenAndOwnerMetadata.')

    def uploadAllTokenAndOwnerMetadata(self):
        owners = FileIO.readFromJSON('owners')
        print(owners)

    # mapping user-principal to nft index
    def downloadAllTokenAndOwnerMetadata_faster(self):
        print('Starting - downloadAllTokenAndOwnerMetadata_faster...')
        listings = self.canister.getRegistry()
        FileIO.writeToPickle('owners_faster', listings[0])
        print('Successful - downloadAllTokenAndOwnerMetadata_faster.')

    def uploadAllTokenAndOwnerMetadata_faster(self):
        data = FileIO.readFromJSON('owners_faster')
        print(data)

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
        print('Starting - downloadAllImages...')
        tokenIndex = 0
        images = []
        iterationSuccess = 0
        while tokenIndex < self.totalTokensSupply:
            try:
                # print('tokenIndex: ', tokenIndex)
                httpRequest = { 'body' : [], 'headers': [], 'method' : 'get', 'url':f"token/{tokenIndex}"}
                res = self.canister.http_request(httpRequest)
                iterationSuccess = 1
            except KeyboardInterrupt: 
                print('User Keyboard Interrupt occured - downloadAllImages. Will exit.')
                return
            except:
                print('Exception occured - downloadAllImages. Will continue and try again.')
                continue
            finally:
                if (iterationSuccess == 1):
                    images.append({'tokenIndex': tokenIndex, 'image': res[0]})
                    tokenIndex = tokenIndex + 1
                    iterationSuccess = 0
        FileIO.writeToPickle('images', images)
        print('Successful - downloadAllImages.')

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

    # download all sales transaction for each token index - slower. use downloadAllTransactions_faster instead
    def downloadAllTransactions(self):
        print('Starting - downloadAllTransactions...')
        tokenIndex = 0
        history = []
        iterationSuccess = 0
        while tokenIndex < self.totalTokensSupply:
            try:
                # print('tokenIndex: ', tokenIndex)
                res = self.canister.getHistory(tokenIndex)
                iterationSuccess = 1
            except KeyboardInterrupt: 
                print('User Keyboard Interrupt occured - downloadAllTransactions. Will exit.')
                return
            except:
                print('Exception occured - downloadAllTransactions. Will continue and try again.')
                continue
            finally:
                if (iterationSuccess == 1):
                    history.append({'tokenIndex': tokenIndex, 'history': res[0]})
                    tokenIndex = tokenIndex + 1
                    iterationSuccess = 0
        FileIO.writeToPickle('history', history)
        print('Successful - downloadAllTransactions.')

    def uploadAllTransactions(self):
        history = FileIO.readFromPickle('history')
        print(history)

    # download all sales transaction in one dump
    def downloadAllTransactions_faster(self):
        print('Starting - downloadAllTransactions_faster...')
        listings = self.canister.getAllSaleRecord()
        FileIO.writeToPickle('history_faster', listings[0])
        print('Successful - downloadAllTransactions_faster.')

    def uploadAllTransactions_faster(self):
        data = FileIO.readFromJSON('history_faster')
        print(data)