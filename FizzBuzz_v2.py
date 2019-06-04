# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:01:00 2019

@author: Jake
"""


"""______________GAME RULES_____________"""

iterations = 20 # how many numbers to play the game with 

def fizzbuzz(val):
    
    if val <=0:
        raise ValueError("The game iteration must be greater than 0" )
    
    if type(val) not in [int]:
        raise TypeError("The game interation must be an integer value")
    
    phrase = ""             
    
    if val % 3 == 0:        #Rule 1: If val is divisible by 3 say "Fizz"
        phrase += "fizz"
    
    if val % 5 == 0:        #Rule 2: If val is divisible by 5 say "Buzz"
        phrase +="buzz"     #Rule 3: if Rule 1+2 both true it says "Fizzbuzz"
     
    if phrase == "":        #(if no rules apply print original val)
        phrase = val
    
    for i in str(val):      #Rule 4: If a val contains a digit of "3" it will override all previous rules with "lucky"
        if int(i) == 3:
            phrase = "lucky"
       
    return phrase 

"""______________IMPLEMENTATION_______________"""


for i in range(iterations): 
    
    print(fizzbuzz(i+1)) # i+1 is basic formatting- translates the output of "range" to "iterations" 
    
