##Hex the string to encrypt
##Hex the key
##Here is a test change

messageraw = "SEXY SEXY FISH HORSE!"
keyraw = "wibbledogwoofwoof"
from first import hexencoder,hex2bin

message = messageraw.rstrip('\r\n')
key = keyraw.rstrip('\r\n')

def main():
            
    messlist = [(hexencoder(i.decode('utf-8', 'ignore').encode('utf-8'))) for i in message]        
    y = len(key)/len(message)
    s = []
    while y < len(messlist):
        for i in key:
            s.append(hexencoder(i))
            y = y + 1
            
    test = [(s[i]) for i in range (len(message))]
    binkey = [(hex2bin(i)) for i in test]
    binmess = [(hex2bin(i)) for i in messlist]  
    
    print (smoosher (''.join(binkey),''.join(binmess)))  

    return main

def smoosher(firstbin,secondbin):   
    
    from first import hexonly
   
    final = [(int(f) ^ int(s)) for f,s in zip(firstbin,secondbin)] 
    finalbin = str(''.join([ '%d'%x for x in final])) ##Final XOR'd binary string. 
    result = hexonly(finalbin)
    
    return result
main()
    
        