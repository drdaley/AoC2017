import math as ma
import sys
inp = float(sys.argv[1]) # get input
n = ma.ceil((ma.sqrt(inp)-1)/2) # number of 'rings' ourwards where [ (1+2n)^2 >= inp ] for the lowest positive n
r_max = (2*n+1)**2 # highest number in the 'ring'
ring = r_max - inp # number of spces on the ring from the highest value to given value
m = abs(ring%(2*n)-n) #The number of steps along the ring 
print('The solution to part 1 is {0}'.format(n+m))