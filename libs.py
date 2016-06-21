def b64encoder(instring): ##hex to ascii

    import base64 
    
    outstuff = base64.encodestring(instring).encode('hex')
    
    return outstuff

def hexencoder(string_in): ##ascii to hex

    a=''
    for x in string_in:
        b = a + ('0'+((hex(ord(x)))[2:]))[-2:]
    
    return b

def hexencoder2(string_in): ##ascii to hex

    hex_string = string_in.encode('hex'.encode('UTF-8'))
    return hex_string

def hex2bin(hexin):
    
    h_size = len(hexin) * 4
    hexin = ( bin(int(hexin, 16))[2:] ).zfill(h_size)
    
    return hexin

def b64decoder(hexin): ##I could have used Python functions here, but this is pretty, and I can see it stepping through the code. 

    ascii_string = ''
    x = 0
    y = 2
    l = len(hexin)
    while y <= l:
        ascii_string += chr(int(hexin[x:y], 16)) ##chr returns ASCII for HEX value
        x += 2
        y += 2
    
    return ascii_string

def b64encoder2(hexin): ##hex to ASCII another way
    ascii_string = hexin.decode('hex'.decode('UTF-8'))
    return ascii_string

def hexr2(binin):
    
    import binascii
    plaintxt = binascii.unhexlify(binin)
    return plaintxt

def hexr(binin):
    
    import re
    hexxed = str('{0:0>4X}'.format(int(binin, 2))) ##Format finalbin as decimal interger, pass to string.

    plaintxt = str(b64decoder(hexxed))
    return plaintxt

def hexonly(binin):
    
    hexxed = str('{0:0>4X}'.format(int(binin, 2))) ##Format finalbin as decimal interger, pass to string.
    return hexxed

def smoosher(firstbin,secondbin):   
   
    final = [(int(f) ^ int(s)) for f,s in zip(firstbin,secondbin)] 
    finalbin = str(''.join([ '%d'%x for x in final])) ##Final XOR'd binary string. 
    result = hexr(finalbin).decode('utf-8', 'ignore').encode('utf-8')
    return result

def writer(a1,a2):
    
    outopen = open(a1,'a')
    outopen.write(a2)
    outopen.write('\n')
    return a2

def main():
    return main

if __name__ == '__main__': 
    main()
