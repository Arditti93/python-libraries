# import random
from random import random, uniform, randint

print(random()) 
# generating a float number between 0 and 1

print(uniform(1,10))
# generate a random float number between the range we specified in the .uniform method

print(randint(1,10)) 
# generate a random int (whole number) betweeen the range we specified in the .randint method


my_num = 50
ran_num =  randint(1,50)

while my_num != ran_num:
    print(f"The number {ran_num} doesn't match my number {my_num}")
    ran_num = randint(1,50)

print(f"The number {ran_num} matches my number {my_num}")