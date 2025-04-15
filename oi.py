import base64, codecs
magic = '\\x68\\x6f\\x6f\\x6b\\x20\\x3d\\x20\\x22'
love_rot13 = codecs.encode("Oi, teste teste teste ...", 'rot_13')
love_base64 = base64.b64encode(love_rot13.encode('utf-8')).decode('utf-8')
love_hex = ''.join([f'\\x{ord(c):02x}' for c in love_base64])
love = f"'{love_hex}'"
god_hex = ''
god = f"'{god_hex}'"
destiny_hex = ''
destiny = f"'{destiny_hex}'"
joy = "'\\x72\\x6f\\x74\\x31\\x33'"
trust = eval(f'"{magic}"') + base64.b64decode(bytes.fromhex('{''.join([hex(ord(c))[2:] for c in eval(love)])})).decode('utf-8') + eval(god) + eval(destiny)
print(trust + '"')
