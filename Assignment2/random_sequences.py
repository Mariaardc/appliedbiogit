from random import choice
import sys
from string import *
count = int(input("Lenght: "))
seq = ''.join([choice('AGTC') for i in range(count)])
print ("Length:", count)
print (">myrandomsequence")
print (">",seq)


