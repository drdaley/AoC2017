f = open('day5_inp.txt')
inp = f.read()
f.close()



sl_inp = inp.split('\n')
l_inp = list(map(int,sl_inp))
#print('l_inp')
pos = 0
steps = 0
while True :
	
	temp_pos = pos
	#print(temp_pos)
	temp_inp = l_inp[temp_pos]
	pos = temp_pos + l_inp[temp_pos]
	if temp_inp >= 3: l_inp[temp_pos] = l_inp[temp_pos]-1
	else: l_inp[temp_pos] = l_inp[temp_pos]+1
	steps = steps+1
	#print(l_inp)
	if pos >= len(l_inp) or pos < 0: break
	
print(steps)