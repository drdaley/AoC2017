held_by = dict()
# parse into (name, holding_list)
for n,h in map(name, hl):
  if h not 0:
    if len(holding_list) == 1: held_by[holding_list] = n
    if len(h) > 1:
      for x in h: held_by[x] = n
for n in n:
  if n not in values.held_by(): print(n)