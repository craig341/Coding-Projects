
#!/bin/python3

# Importing some useful libraries
import math
import os
import random
import re
import sys

def solution(n):
	if (1<= n <= 100):
		if(n % 2 == 1): 
			return("Weird")
    
		elif(n % 2 == 0 and 2<= n <= 5): 
			return("Not Weird") 
		
		elif(n % 2 == 0 and 6<= n <= 20): 
			return("Weird") 
		
		elif(n % 2 == 0 and n > 20): 
			return("Not Weird")
		
    

if __name__ == '__main__':
    n = int(input().strip()) # This line will read an integer inserted by the user and store it into a variable called n, which is then passed to your solution function as an argument

    print(solution(n)) # calls the solution function with the value you insert