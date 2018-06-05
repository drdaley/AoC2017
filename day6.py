#Create inp
ini_inp = list([4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5])
inp = ini_inp
s = 0
#Find largest value in inp
while True:
	find_val = sorted(inp)
	ind_val = inp.index(find_val[0]) #index of the largest value
	print(ind_val)
	inp[ind_val] = 0 # set value = 0
	for n in list(range(1,(find_val[0]+1))):
		index = int((ind_val+n)%len(ini_inp))
		inp[index] = inp[index]+1
	s = s+1
	print(inp)
	if inp[:] is ini_inp[:]: break
print(s)
