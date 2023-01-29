from backupNft import *

srcNftCanisterId = '2x3lw-tiaaa-aaaah-qcvca-cai' 
srcMetadataCanisterId = 'v4oyv-zaaaa-aaaah-qctya-cai'
srcStorageCanisterId = '2q2nc-6qaaa-aaaah-qcvcq-cai'
totalTokensSupply = 10000
downloadMetadata = 1

performBackUp(
    'dfinityGangs', 
    srcNftCanisterId, 'v1', downloadMetadata,
    srcMetadataCanisterId, 
    srcStorageCanisterId, 
    totalTokensSupply)