from bitcoin.rpc import RawProxy

p = RawProxy()

raw_tx = p.getrawtransaction(raw_input('Transakcijos id: '))

decoded_tx = p.decoderawtransaction(raw_tx)

ivestis=0
iseiga=0
 
for v in decoded_tx['vin']:
    neapdorotaIvestis = p.getrawtransaction(v['txid'])
    apdorotaIvestis = p.decoderawtransaction(neapdorotaIvestis)
        
    rezultatas = apdorotaIvestis['vout'][v['vout']]
    ivestis += rezultatas['value']

for v in decoded_tx['vout']:
    iseiga += v['value']
    
print("%s %s" % ("Transakcijos mokestis:", ivestis - iseiga))