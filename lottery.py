#!/usr/bin/python3

from threading import Thread
import time
import random
import struct
import os
import sys
from getpass import getpass

print("""
Welcome... the lottery is started... please press CTRL + C to stop
""")


def waktu(det, byk):
 ank = byk
 for aka in range(byk):
  print(byk, end='\r')
  time.sleep(det)
sudah = [] 
def undian():
 try:
  benar = 1
  while benar == 1:
#   print(' ')    

   hasil = (random.randint(1, 40))
   sudah.append(hasil)
   print(hasil, end='\r')
#   print(' ')
   time.sleep(0.1)
 except KeyboardInterrupt:
  try:
   if sys.argv[1] == "a":
    if (hasil in sudah):
     print("Sudah keluar tadi...lanjut")
     undian()
  except:
   pass

  print('\n')
  print(random.randint(1, 40))
  print(' ')
  exit()

mantap = Thread(target = waktu, args = [5, 5])
undian() 		
sys.exit()

 
