#!/usr/bin/python

# Function definition is here
import random    
def getRandomArray(n):
   nums = random.sample(range(0,100000),n)
   print nums
   return;


def getSortedArray(n):
    nums = []
    for i in range (n):
        nums.append(n)
        n = n-1
    print nums
    return;

