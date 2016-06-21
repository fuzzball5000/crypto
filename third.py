h = '22070B0103170A4347161D0A460E001A46000103164C0D051F1712011C4600070A085708422C0D171307061B4F02071C0A1C46041E07071849441C10120A1B461B001903571D0D420D450C0015040A50'
h2 = 'c:/users/richag2/Desktop/playtime/ascii.csv'

from first import hex2bin,hexencoder,smoosher

import csv

def main():
    
    reslist = {}
    x = 0
    r = csv.reader(open(h2))
    test = sum(1 for row in open(h2))
    
    while test > x:
        
        h2ascii=''.join(r.next())      
        hbin = hex2bin(h)
        
        for i in (h2ascii):
            binh2list = [((hex2bin(hexencoder(i)))) for i in h2ascii]
        
        num = len(hbin)/8
        d = 0
        
        repeatlist = []
        while d < num:
            repeatlist.append(''.join(binh2list))
            d = d + 1
        
        reslist.update({(h2ascii,smoosher([i for i in hbin],[i for i in ''.join(repeatlist)]))}) ## Make list of single bin chars [1],[0] from 8 bit stings in previos list [01010101]
        x = x + 1

    for a,b in reslist.iteritems():
        tempstr = ''.join(b)
        charstr = 'etaoin'
        sensit = len(charstr)+len(b)/len(charstr)
        if (sum(tempstr.count(c) for c in charstr)) >= sensit:
            print a,(b),'*',sensit,'*'
    return main

        
if __name__ == '__main__': 
    main()
    
    
    