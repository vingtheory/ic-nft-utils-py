from CCCCanisterUtils import *

def performBackUp(
    collectionName, 
    srcNftCanisterId, nftCandidVersion, downloadMetadata,
    srcMetadataCanisterId, 
    srcStorageCanisterId, 
    totalTokensSupply):
    
    cccNFTCanisterUtils = CCCNFTCanisterUtils(collectionName, srcNftCanisterId, totalTokensSupply, nftCandidVersion)
    print('JOB STARTING.')

    print('(1/7) - Downloading owners and holdings of all tokens...')
    # owners and holdings of all tokens
    cccNFTCanisterUtils.downloadAllTokenAndOwnerMetadata_faster()
    # cccNFTCanisterUtils.uploadAllTokenAndOwnerMetadata_faster()

    print('(2/7) - Downloading all tokens - metadata, traits, rarity...')
    # all tokens - metadata, traits, rarity
    if(downloadMetadata == 1) : cccNFTCanisterUtils.downloadAllTokensMetadata()
    # cccNFTCanisterUtils.uploadAllTokensMetadata()

    print('(3/7) - Downloading all component info - all trait and rarity...')
    # all component info - all trait and rarity 
    if(downloadMetadata == 1) : cccNFTCanisterUtils.downloadAllComponentsInfo()
    # cccNFTCanisterUtils.uploadAllComponentsInfo()

    print('(4/7) - Downloading current listings...')
    # current listings
    cccNFTCanisterUtils.downloadAllListings()
    # cccNFTCanisterUtils.uploadAllListings()

    print('(5/7) - Downloading sold listings...')
    # sold listings
    cccNFTCanisterUtils.downloadAllSoldListings()
    # cccNFTCanisterUtils.uploadAllSoldListings()

    if(srcMetadataCanisterId != 'ipfs') : 
        cccNFTMetadataCanisterUtils = CCCNFTMetadataCanisterUtils(collectionName, srcMetadataCanisterId, totalTokensSupply)
        print('(6/7) - Downloading all images...')
        cccNFTMetadataCanisterUtils.downloadAllImages()
        # cccNFTMetadataCanisterUtils.uploadAllImages()
    elif(srcMetadataCanisterId == 'ipfs') : 
        cccNFTCanisterUtils.downloadImageReferenceData()

    cccStorageCanisterUtils = CCCNFTStorageCanisterUtils(collectionName, srcStorageCanisterId, totalTokensSupply)
    print('(7/7) - Downloading all transactions...')
    cccStorageCanisterUtils.downloadAllTransactions_faster()
    # cccStorageCanisterUtils.uploadAllTransactions_faster()

    print('JOB COMPLETE.')