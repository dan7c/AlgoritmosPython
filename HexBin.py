## Numero a ser convertido deve ser passado no terminal: 
## EX: python HexBin.py NUM

import sys;
arg = int(sys.argv[1])

numeroHex = []
numeroBin = []

def toHex(num):
  if(num > 0):
    if(num%16 == 10):
      numeroHex.insert(0, 'A')
    if(num%16 == 11):
      numeroHex.insert(0, 'B')
    if(num%16 == 12):
      numeroHex.insert(0, 'C')
    if(num%16 == 13):
      numeroHex.insert(0, 'D')
    if(num%16 == 14):
      numeroHex.insert(0, 'E')
    if(num%16 == 15):
      numeroHex.insert(0, 'F')
  
    if(num%16 < 10):
      numeroHex.insert(0, num%16)      
    
    return toHex(num//16)     

def toBin(num):
  if(num != 0):
    numeroBin.insert(0, num%2)
    return toBin(num//2)     


toBin(arg)
print('Binário: ' + ''.join(str(n) for n in numeroBin))

toHex(arg)
print('Hexadecimal: ' + ''.join(str(n) for n in numeroHex))