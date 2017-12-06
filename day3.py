import math as ma
import sys
inp = float(sys.argv[1]) # get input
n = ma.ceil((ma.sqrt(inp)-1)/2) # number of 'rings' ourwards where [ (1+2n)^2 >= inp ] for the lowest positive n
r_max = (2*n+1)**2 # highest number in the 'ring'
ring = r_max - inp # number of spces on the ring from the highest value to given value
m = abs(ring%(2*n)-n) #The number of steps along the ring
# m should be applicable to the grid issue

# begin part 2 
def xy_coord(steps,n): #given a number of steps around a ring and the 'n' value of the ring, gives a tuple (x,y)
	if steps <= 2*n: return (n, -n+steps)
	elif steps > 2*n and steps <= 4*n : return (int(n-(steps-2*n)) , n)
	elif steps > 4*n and steps <= 6*n : return (-n,n-(steps-4*n))
	elif steps > 6*n : return (-n+(steps-6*n),-n)
	else: print('xy_coord sanity fail')

def gen_adjacent(xy):
	hits = list()
	pm1 = list(range(-1,2))
	#print(xy)
	for n in pm1:
		for m in pm1:
			#print(xy)
			#print((xy[0]+m,xy[1]+n))
			if (xy[0]+m,xy[1]+n) != xy : hits.append((xy[0]+m,xy[1]+n))
	return hits
	
def find_val(grid, adj):
	vals = list()
	for a in adj:
		if a in grid.keys(): vals.append(grid[a])
		else:pass
	return sum(vals)

grid = dict()
grid[(0,0)] = 1
n=0
found = False
while True: 
	if found == True : break
	else: pass
	n=n+1
	circ = 8*n
	steps = 0
	while steps <= circ :
		steps= steps+1
		print(gen_adjacent(xy_coord(steps,n)))
		grid[xy_coord(steps,n)] = find_val(grid, gen_adjacent(xy_coord(steps,n))) # Hmmmmmm
		if grid[xy_coord(steps,n)] >= inp : 
			found = True
			solution = grid[xy_coord(steps,n)]
			break
#def y_coord(steps,n):
#	if steps <= 2*n: return -n+steps
#	elif steps > 2*n and steps <= 4*n : return n
#	elif steps > 4*n and steps <= 6*n : return (n-(steps%(2*n)))
#	elif steps > 6*n : return -n
#	else: print('y_coord sanity fail')
#print(grid)

print('The solution to part 1 is {0}'.format(n+m))
print(solution)