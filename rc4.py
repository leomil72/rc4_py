## RC 4 Algorithm
# Written in Python 3.x
# by Leonardo Miliani (2023)
#
# Version 1.0 (20230618)

import sys

# create empty s-box and indexes
sbox = [0] * 256
p = q = 0

def keySchedule(key):
    ## Key schedule
    global p, q, sbox
    # populate sbox
    sbox = [n for n in range(256)]
    # reset indexes
    p = q = j = 0
    # get key length
    ln = len(key)
    # repeat 256 times
    for i in range(256):
        j = (j + sbox[i] + key[i % ln]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]

def byteGenerator():
    ## generate a byte from the key stream
    global p, q, state
    p = (p + 1) % 256
    q = (q + sbox[p]) % 256
    sbox[p], sbox[q] = sbox[q], sbox[p]
    return sbox[(sbox[p] + sbox[q]) % 256]

def crypto(key, text):
    ## encryption/decryption function
    # initialize keystream
    keySchedule(string_to_list(key))
    # return bytes stream
    return [ord(p) ^ byteGenerator() for p in text]

def string_to_list(inputString):
    ## convert string into a byte list
    return [ord(c) for c in inputString]

def printhex(txt):
    ## print byte list in hex values
    res = ''
    # works only with non-empty strings
    if type(txt) is str and txt != '':
        for c in txt:
            res += ''.join('{:02X}'.format(ord(c)))
    return res

def main(argv):
    ## RC4 algorithm
    print('RC4 ALGORITHM\n')

    # ask for a key
    tmpKey = input('Enter key (w/o spaces): ')
    tmpKey.replace(' ', '')
    if (tmpKey == ''):
        return
    # only 256 chars
    if (len(tmpKey) > 255):
        tmpKey = tmpKey[:256]
    # ask for text
    tmpTxt = input('Text to encrypt: ')
    if (tmpTxt == ''):
        return
    # encrypt text
    encrypt = crypto(tmpKey, tmpTxt)
    encryptText = [chr(a) for a in encrypt]
    print('ENCRYPTION:')
    # print encryption as a byte list
    print(encrypt)
    # print encryption as a char list
    print(encryptText)
    # print encryption in hex values
    encryptText = ''.join([chr(a) for a in encrypt])
    print(printhex(encryptText))
    print('DECRYPTION:')
    decrypt = crypto(tmpKey, encryptText)
    decryptText = ''.join([chr(a) for a in decrypt])
    # print decryption as a byte list
    print(decrypt)
    # print encryption as a string
    print(decryptText)

# run only when explicitely launched
if __name__ == "__main__":
    main(sys.argv)
    print("\nTERMINATED")
