from backupNft import *

srcNftCanisterId = 'o7ehd-5qaaa-aaaah-qc2zq-cai' 
srcMetadataCanisterId = 'ipfs'
srcStorageCanisterId = 'okdwo-4yaaa-aaaah-qc22a-cai'
totalTokensSupply = 10000
downloadMetadata = 0

performBackUp(
    'ICCyberSkulls', 
    srcNftCanisterId, 'v2', downloadMetadata,
    srcMetadataCanisterId, 
    srcStorageCanisterId, 
    totalTokensSupply)