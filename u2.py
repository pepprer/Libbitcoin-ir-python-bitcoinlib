import hashlib
from bitcoin.rpc import RawProxy
from bitcoin.core import lx, b2x, b2lx

p = RawProxy()

blokas = p.getblock(p.getblockhash(int(raw_input('Iveskite bloko auksti: '))))

headeris = (
    b2x(lx(blokas['versionHex']))
    + b2x(lx(blokas['previousblockhash'] if 'previousblockhash' in blokas else '0' * 64))
    + b2x(lx(blokas['merkleroot']))
    + b2x(lx("%08x" % blokas['time']))
    + b2x(lx(blokas['bits']))
    + b2x(lx("%08x" % blokas['nonce']))
    )

headerioBaitai = headeris.decode('hex')

hashas = hashlib.sha256(hashlib.sha256(headerioBaitai).digest()).digest()

hashas = hashas[::-1].encode('hex_codec')

if hashas == blokas['hash']:
    print('Teisingas')
else:
    print('Neteisingas')

