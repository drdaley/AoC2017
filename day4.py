def pass_test(phrase):
	p_list = phrase.split(' ')
	pf = list()
	for w in p_list:
		a = p_list.count(w)
		if a > 1 : pf.append(0)
		else : pf.append(1)
	if len(pf) < len(p_list) : print('pass/fail list error')
	if all(pf) : return True
	else: return False