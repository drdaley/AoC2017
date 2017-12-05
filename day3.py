import math as ma
import sys
#import sympy
#from sympy.solvers import solve
inp = float(sys.argv[1])
#n = sympy.Symbol('n', positive=True)
#n_val = solve(((1+2n)^2) == 12 ,n)
n = ma.ceil((ma.sqrt(inp)-1)/2) # number of 'rings' ourwards where [ (1+2n)^2 >= inp ] for the lowest positive n
len = (2*n+1) # length of the side
r_max = (2*n+1)**2 # highest number in the 'ring'
print(r_max)
ring = r_max - inp 
print(abs(ring%(2*n)-n))
m = abs(ring%(2*n)-n) #The number of steps along the ring 

print(ring)
print(n)
print('The solution to part 1 is {0}'.format(n+m))