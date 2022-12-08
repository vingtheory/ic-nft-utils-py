from CCCCanisterUtils import *

srcNftCanisterId = '2x3lw-tiaaa-aaaah-qcvca-cai'
srcMetadataCanisterId = 'v4oyv-zaaaa-aaaah-qctya-cai'
srcStorageCanisterId = '2q2nc-6qaaa-aaaah-qcvcq-cai'
totalTokensSupply = 10000

cccNFTCanisterUtils = CCCNFTCanisterUtils('dfinityGangs', srcNftCanisterId, totalTokensSupply)
cccNFTCanisterUtils.downloadAllTokenAndOwnerMetadata()
cccNFTCanisterUtils.uploadAllTokenAndOwnerMetadata()
cccNFTCanisterUtils.downloadAllTokenAndOwnerMetadata()
cccNFTCanisterUtils.downloadAllListings()
cccNFTCanisterUtils.uploadAllListings()
cccNFTCanisterUtils.downloadTokensMetadata()
cccNFTCanisterUtils.downloadAllComponentsInfo()
cccNFTCanisterUtils.uploadAllComponentsInfo()
cccNFTCanisterUtils.downloadAllTokensMetadata()
cccNFTCanisterUtils.uploadAllTokensMetadata()

cccNFTMetadataCanisterUtils = CCCNFTMetadataCanisterUtils('dfinityGangs', srcMetadataCanisterId, totalTokensSupply)
cccNFTMetadataCanisterUtils.downloadAllImages()
cccNFTMetadataCanisterUtils.uploadAllImages()

cccStorageCanisterUtils = CCCNFTStorageCanisterUtils('dfinityGangs', srcStorageCanisterId, totalTokensSupply)
cccStorageCanisterUtils.downloadAllTransactions()
cccStorageCanisterUtils.uploadAllTransactions()

