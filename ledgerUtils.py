import hashlib
import zlib
from ic.principal import Principal

CRC_LENGTH_IN_BYTES = 4

def createSubAccountId(stakerPrincipal, secretPhrase) : 
        sha224 = hashlib.sha224()
        sha224.update(secretPhrase)
        sha224.update(Principal.from_str(stakerPrincipal).bytes)
        hash = sha224.digest()
        checksum = zlib.crc32(hash) & 0xFFFFFFFF
        account = checksum.to_bytes(CRC_LENGTH_IN_BYTES, byteorder='big') + hash
        return [x for x in account]