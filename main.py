# -*- coding: utf-8 -*-
"""
SMHI_DATA DIAGRAM

Explanation: ???
    
Help: ???
    
Desc: ???
    
"""
from functions import makeplot

print ("WELCOME TO THE DEPTHSNOW DIAGRAM")
print ("Please enter which file you wanna use")
print ("Must be filename+exenstion type, E.g DATA.scv")

fileName=input("type file: ")
makeplot(fileName)


print("Program ENDS HERE")
