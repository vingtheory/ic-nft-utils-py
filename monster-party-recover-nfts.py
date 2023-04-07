from nftUtils import NFTUtils
from ledgerUtils import createSubAccountId

# targetPrincipal = 'zc4pb-tfqtw-olj3q-j7vm3-63ebk-5jckq-22god-hkqka-vcyhg-jqh74-mqe'
# fromAddress = '7448781cb9d44997c5bff40a8449ec394ed2338ee36d62d9a276c3d7f794a677' 
# toAddress = '7936499b71a4a41a15abc4ec52f972ac1756432763394bf35799287a1aa35c39'
# tokenId = 'kpd66-qakor-uwiaa-aaaaa-buamv-qaqca-aaaa4-a'
# canisterId = 't3lq2-raaaa-aaaag-qbswa-cai'
# subAccount = createSubAccountId(targetPrincipal, b'staker')

targetPrincipal = 'h5o7k-xcwym-7sqju-7ocxp-xzyvj-53hve-si4ex-gyzyb-c6ek6-bbfmq-6qe'
fromAddress = '5f4d828ad35da23bc35132425d986771fe9dd20cb18ceb873b3286ab49ea361e' 
toAddress = 'ed04989a0fb433f26d9faf981ca0e132a5515a3000eaec7ca0370e5ca1694d75'
tokenId = '56zyb-bqkor-uwiaa-aaaaa-b4awo-iaqca-aaaaa-a'
canisterId = '46sy3-aiaaa-aaaah-qczza-cai'
subAccount = createSubAccountId(targetPrincipal, b'staker')

def recover():
    nftUtils = NFTUtils('ext', canisterId)
    nftUtils.recover(fromAddress, toAddress, tokenId, subAccount)

recover()