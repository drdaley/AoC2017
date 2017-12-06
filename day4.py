def pass_test(phrase): # given a phrase, returns true if the phrase passes, else false
	phrase = phrase.rstrip('\n')
	p_list = phrase.split(' ')
	print(p_list)
	pf = list()
	for w in p_list:
		a = p_list.count(w)
		if a > 1 : pf.append(0)
		else : pf.append(1)
	if len(pf) < len(p_list) : print('pass/fail list error')
	if all(pf) : return True
	else: return False

f = open('day4_inp.txt')
inp = f.readlines()
f.close()

valid = list()

for phrase in inp:
	print(phrase)
	print(pass_test(phrase))
	valid.append(pass_test(phrase))

print(len(inp))
print(len(valid))
print(sum(valid))