#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:27:44 2023

@author: charan
"""
l=[]
e=[]
x=int(input("Enter no.of elements in list:"))
for j in range(x):
    y=int(input("Enter the element:"))
    l.append(y)
print (l)
sum=0
for i in l:
    sum+=i
print("sum of elements:",sum)
print("maximum value is:",max(l))
for i in l:
    if(i%2==0):
      e.append(i)
print("Even list",e)
