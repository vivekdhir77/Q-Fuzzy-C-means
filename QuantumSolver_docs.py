from Quantum_solver import *
from functions import *
import math

def fun(x):
    return math.cos(x)

def search_Area(s):
    if(s==1):
        return random.uniform(0, math.radians(90)/2)
    elif(s==2):
        return random.uniform(math.radians(90)/2, math.radians(90))
    elif(s==3):
        return random.uniform(math.radians(90), (math.radians(90)*3)/2)
    elif(s==4):
        return random.uniform((math.radians(90)*3)/2, math.radians(180))

f = [0.707 for i in range(2)]
quant = Quantum_solver(extremum=0, features = f) # we are trying to minimize
search_space = quant.solver()
Ygen = fun(search_Area(search_space+1))# 0 - 0.25
print(Ygen)

for i in range(1000):
    search_space= quant.solver(Ygen)
    Ygen = fun(search_area(search_space+1))
    print(Ygen)
print()
print(quant.best())

# 
# The constructor will take the following arguments
# 1. features 
#    => data type - list of floats 
#    => You are required to give a list of values between (0,1)
# 
# 2. extremum
#    => byte => 0 or 1
#    => 0 in case you're trying to go towards minimum. 1 in case you're trying to go towards maximum. 
#    => Default argument is 1.
# 
# 3. rand_solve
#    => boolean
#    => True in case you're trying use the random method [r as a random number, list] .
#       False in case you're trying use the Quantum rotation method [r as a q bit, list] 
#    => Default argument is True
#
#
# functions in the Class Quantum_solver
# solver-  
#       -It has the following argument
#           fitness - 1. You will have to input the fitness value for every iteration to get a better binary list
#                     2. Defalut fintess value is 0

