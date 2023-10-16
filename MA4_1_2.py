import math
import random

V_d = lambda d : (math.pi**(d/2))/math.gamma(d/2+1) # used lambda
square_d = lambda d: 2**d

n = 100000

dimension = [2, 11] # can change if you want to calculate other dimension

exact_value = [ V_d(i) for i in dimension] # used list comprehension


print('exact value (dim, value) : \t', end='')
print(list(zip(dimension,exact_value))) # used zip()

approximation = []


for d in dimension:
    n_c = 0
    for _ in range(n):
        if sum([random.uniform(-1,1)**2 for _ in range(d)]) <= 1:
            n_c+=1
    approximation.append(square_d(d)*n_c/n)
    

print('approximation (dim, value) : \t', end='')         
print(list(zip(dimension,approximation)))
