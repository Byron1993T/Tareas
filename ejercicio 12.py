# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:43:48 2020

@author: CEC
"""

def isPrime (num):
  if num<2:
    return False
  for i in range(2,num):
    if num % i==0:
      return False
  return True
isPrime(7)

def isPrime (num):
  if num<2:
    return False
  for i in range(2,num):
    if num % i==0:
      return False
  return True
isPrime(7)
for i in range(1,20):
  if isPrime(i+1):
    print(i+1,end=" ")
print()