from CCCCanisterUtils import *

srcNftCanisterId = '2x3lw-tiaaa-aaaah-qcvca-cai' 
srcMetadataCanisterId = 'v4oyv-zaaaa-aaaah-qctya-cai'
srcStorageCanisterId = '2q2nc-6qaaa-aaaah-qcvcq-cai'
totalTokensSupply = 10000

cccNFTCanisterUtils = CCCNFTCanisterUtils('dfinityGangs', srcNftCanisterId, totalTokensSupply)

print('JOB STARTING.')

print('(1/7) - Downloading owners and holdings of all tokens...')
# owners and holdings of all tokens
cccNFTCanisterUtils.downloadAllTokenAndOwnerMetadata_faster()
# cccNFTCanisterUtils.uploadAllTokenAndOwnerMetadata_faster()

print('(2/7) - Downloading all tokens - metadata, traits, rarity...')
# all tokens - metadata, traits, rarity
cccNFTCanisterUtils.downloadAllTokensMetadata()
# cccNFTCanisterUtils.uploadAllTokensMetadata()

print('(3/7) - Downloading all component info - all trait and rarity...')
# all component info - all trait and rarity 
cccNFTCanisterUtils.downloadAllComponentsInfo()
# cccNFTCanisterUtils.uploadAllComponentsInfo()

print('(4/7) - Downloading current listings...')
# current listings
cccNFTCanisterUtils.downloadAllListings()
# cccNFTCanisterUtils.uploadAllListings()

print('(5/7) - Downloading sold listings...')
# sold listings
cccNFTCanisterUtils.downloadAllSoldListings()
# cccNFTCanisterUtils.uploadAllSoldListings()

cccNFTMetadataCanisterUtils = CCCNFTMetadataCanisterUtils('dfinityGangs', srcMetadataCanisterId, totalTokensSupply)

print('(6/7) - Downloading all images...')
cccNFTMetadataCanisterUtils.downloadAllImages()
# cccNFTMetadataCanisterUtils.uploadAllImages()

cccStorageCanisterUtils = CCCNFTStorageCanisterUtils('dfinityGangs', srcStorageCanisterId, totalTokensSupply)

print('(7/7) - Downloading all transactions...')
cccStorageCanisterUtils.downloadAllTransactions_faster()
# cccStorageCanisterUtils.uploadAllTransactions_faster()

print('JOB COMPLETE.')

