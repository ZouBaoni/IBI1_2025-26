# What does this piece of code do?
# Answer: This code generates 11 random integers between 1 and 10, and calculates and outputs their total sum.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0 #define a variable
progress=0 #define a variable to control the loop times
#do this for 11 times
while progress<=10:
	progress+=1
	n = randint(1,10) #draw a random number between 1 and 10
	total_rand+=n #add the random number to total_rand

print(total_rand)
