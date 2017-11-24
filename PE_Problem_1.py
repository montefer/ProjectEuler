# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 13:44:59 2017

@author: Fernando Montes
"""
import math

#If we list all the natural numbers below ten that are multiples
#of 3 or 5, we get 3,5,6, and 9. The sum of these numbers is 23.
#Find the sum of all multiples of 3 or 5 below 1000

if __name__ == "__main__":
    upper_limit = 999#(int(input("Find the sum of all multiples of 3 or 5 below...: ? "))-1)
    sum_of_threes = ((3+math.floor(upper_limit/3)*3)/2)*math.floor(upper_limit/3)
    sum_of_fives = ((5+math.floor(upper_limit/5)*5)/2)*math.floor(upper_limit/5)
    multiples_of_three_and_five = ((15+math.floor(upper_limit/15)*15)/2)*math.floor(upper_limit/15)
    
    total_sum = sum_of_threes+sum_of_fives-multiples_of_three_and_five
    print(int(total_sum))