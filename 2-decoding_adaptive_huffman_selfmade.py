
import math
import os
import time
import sys
import re
#entery = 00110100110101010110010111101001111

while True:
    entery=str(input("please insert your demanding binary code OR type 'exit' : "))
    if entery=="exit":
        break
    entery_1=str(input("please insert your demanding character for 1: "))
    entery_2=str(input("please insert your demanding character for 01: "))
    entery_3=str(input("please insert your demanding character for 001: "))


    
    convert_all_entery = entery.replace('001',entery_3)
    convert_all_entery1 = convert_all_entery.replace('01',entery_2)
    convert_all_entery2 = convert_all_entery1.replace('1',entery_1)
    print("decoded data with adaptive huffman source coding is :\n",convert_all_entery2)

#abcabccccbacbbbcabbb
print("please wait , You Are Getting Out...")
input()