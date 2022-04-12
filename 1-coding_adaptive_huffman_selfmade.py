import math
import os
import time
import sys
import re
#entery = abcabccccbacbbbcabbb
#abcabccccbacbbbcabbb
a_we=0
b_we=0
c_we=0
root_we=0

while True:
    entery=str(input("please insert your demanding data with 3 characters (abc)  OR type 'exit' : "))
    if entery=="exit":
        break
    for item in entery:
        if item=="a" :
            root_we+=1
            a_we+=1
        elif item=="b" :
            root_we+=1
            b_we+=1
        elif item=="c" :
            root_we+=1
            c_we+=1
  
    print("root weight = ",root_we,"a weight = ",a_we,"b weight = ",b_we,"c weight = ",c_we)    
    #detecting maximum weight analised
    num1=num2=num3=0
    li=list()
    li.append(a_we)
    li.append(b_we)
    li.append(c_we)

    li.sort()
    num1=li[2]
    num2=li[1]
    num3=li[0]
    print("the character related to ",num1,"will be 1")
    print("the character related to ",num2,"will be 01")
    print("the character related to ",num3,"will be 001")
    
    if num1==b_we and num2==c_we and num3==a_we :
        convert_all_entery = entery.replace('b','1')
        convert_all_entery1 = convert_all_entery.replace('c','01')
        convert_all_entery2 = convert_all_entery1.replace('a','001')
        print("converted data with adaptive huffman source coding is :\n",convert_all_entery2)
    if num1==c_we and num2==a_we and num3==b_we :
        convert_all_entery = entery.replace('c','1')
        convert_all_entery1 = convert_all_entery.replace('a','01')
        convert_all_entery2 = convert_all_entery1.replace('b','001')
        print("converted data with adaptive huffman source coding is :\n",convert_all_entery2)
    if num1==a_we and num2==b_we and num3==c_we :
        convert_all_entery = entery.replace('a','1')
        convert_all_entery1 = convert_all_entery.replace('b','01')
        convert_all_entery2 = convert_all_entery1.replace('c','001')
        print("converted data with adaptive huffman source coding is :\n",convert_all_entery2)
    if num1==c_we and num2==b_we and num3==a_we :
        convert_all_entery = entery.replace('c','1')
        convert_all_entery1 = convert_all_entery.replace('b','01')
        convert_all_entery2 = convert_all_entery1.replace('a','001')
        print("converted data with adaptive huffman source coding is :\n",convert_all_entery2)
    if num1==a_we and num2==c_we and num3==b_we :
        convert_all_entery = entery.replace('a','1')
        convert_all_entery1 = convert_all_entery.replace('c','01')
        convert_all_entery2 = convert_all_entery1.replace('b','001')
        print("converted data with adaptive huffman source coding is :\n",convert_all_entery2)
    if num1==b_we and num2==a_we and num3==c_we :
        convert_all_entery = entery.replace('b','1')
        convert_all_entery1 = convert_all_entery.replace('a','01')
        convert_all_entery2 = convert_all_entery1.replace('c','001')
        print("coded data with adaptive huffman source coding is :\n",convert_all_entery2)

#00110100110101010110010111101001111
print("please wait , You Are Getting Out...")
input()