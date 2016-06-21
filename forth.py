hopen = 'c:/users/richag2/Desktop/playtime/gistfile2.txt'
keys = 'c:/users/richag2/Desktop/playtime/ascii.csv'
outfile = 'c:/users/richag2/Desktop/playtime/blah.txt'

from first import hex2bin,hexencoder,smoosher,writer

import csv

def main():

    reslist = {}
    with open(hopen) as f:
        for line in f:
            ##open CSV secret file, read in each row. For each row.
            linen = line.rstrip('\r\n')
            ##Strip out newline and CR bollocks from the secret string.

            x = 0
            r = csv.reader(open(keys))

            while sum(1 for i in open(keys)) > x:
                ##Count lines in ASCII key file file
                keysascii=''.join(r.next())
                ##each line in key file as string

                binkeyslist = [(hex2bin(hexencoder(key))) for key in (keysascii)]
                ##List each char in ASCII file as HEX then BIN into a list of
                ##8bit bin for each char

                d = 0
                repeatkeylist = []
                while d < len(hex2bin(linen))/8:
                    repeatkeylist.append(''.join(binkeyslist))
                    ##repeat the joined key string (for >1 char keys)into new
                    ##list for len of secrectbin/8, so length is same as secret
                    d = d + 1

                repeatlistsingle = [i for i in ''.join(repeatkeylist)]
                secbinsingle = [i for i in hex2bin(linen)]
                ## Make list of single bin chars [1],[0] from each item
                ##in SECRET file.

                reslist.update({keysascii:smoosher(secbinsingle,repeatlistsingle)})
                ##Add ASCII 'key' value to XOR'd result of Key and Secret.

                x = x + 1

            for a,b in reslist.iteritems():

                charstring2 = 'etaoin'##Most freqent letters in English sentances
                sensitB = len(charstring2)+len(b)/len(charstring2)
                ## Get interger based on length of key, secret, and some attempt at normalising.
                wibble = (sum((''.join(b.decode('utf-8', 'ignore').encode('utf-8'))).count(c) for c in charstring2))
                ##Count how many times letters show up in decrypted string
                output = a,b,wibble,linen

                if wibble >= sensitB: ##if amount of valid chars in decrypted
                ##secret is equal to or more than metric.
                    print output,sensitB
                    outstr = str(output)
                    ##writer(outfile,outstr)
    f.close

    return main

if __name__ == '__main__':
    main()
