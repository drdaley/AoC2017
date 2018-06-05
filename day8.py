# parse
file = open()
lines = file.readlines()
file.close()
parsed_lines = list()
for line in lines:
  parsed_lines.append(line.rstrip('\n').split(' '))
#parse lines, [0] is reg to be changed, [1] is the sign, [2] is magnitude, skip [3], [4] is condition reg, [5] and [6] are contition
#time for eval?
for pl in parsed_lines:
  if eval('{0} {1} {2}',format(pl[4], pl[5], pl[6])):
    if pl[1] == 'inc' : 
      eval('{0} = {0} + {1}'.format(pl[0],pl[2]))
    elif pl[1] == 'dec' :
      eval('{0} = {0} + {1}'.format(pl[0],pl[2]))
    else: print('Inc/dec sanity fail.')