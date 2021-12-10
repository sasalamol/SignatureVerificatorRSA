#RSA248 ISO/IEC 9796 Signature Verificator
#Author: Semih Aslan SAGLAMOL 
#sasalamol

from Crypto.PublicKey import RSA
import pem
import time
from time import sleep
import sys

cer = input('Enter the cer file name for the public key:  ')
signhex = input('Enter the signature:  ')
sha = input('Enter the hash value:  ')
sign = int(signhex,16)
key = pem.parse_file(cer)
print("certificate imported:\n", str(key[0]))
pub = RSA.import_key(open(cer).read())
print(pub)
print("modulus:", pub.n)
print("encryption key:", pub.e)
sub = pub.n - sign
sys.stdout.write ('Just a sec!\nVerification in progress') ;
data1 = pow(sign,pub.e) % pub.n
result = hex(data1)
print("sigend hash" , result[447:])
print("original hash" , sha)

 if result[447:] == sha :
  print("SIGNATURE VERIFIED")
  else :
   print("NOT VERIFIED")
