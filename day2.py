import collections as co

def div_test(a, b):
  if (b/a).is_integer(): return True
  else:return False
  
  
f = open("./day2_inp.txt", 'r')
inp_lines = f.readlines()
f.close()

hilo = list()
lines = list()
for l in inp_lines: # change the readlines input into a 2d list, containing the entries as integers
  m = l.split('\t')
  n = list(map(int, m))
  lines.append(n)

for n in lines:  # find the highest and lowest values in each line and collect them in hilo
  o = sorted(n)
  hilo.append((o[0],o[-1]))

#print(hilo) # sanity check
abs_delta= list()
divisors = list()
print(lines)
for line in lines:
  dq = co.deque(line)
  #print(dq)
  #print(list(range(1,len(dq))))
  for n in list(range(len(dq))):
    for b in list(range(1,len(dq))): # I learned that slicing deques is a no go
      if div_test(dq[0], dq[b]): 
        print(div_test(dq[0], dq[b]))
        print(int(dq[b]/dq[0]))
        divisors.append(dq[b]/dq[0])
    dq.rotate(-1)

for l,h in hilo:
  abs_delta.append(abs(h-l))
#print(abs_delta) # sanity check
print(divisors)
print("The solution to part 1 is {0}. The solution to part 2 is {1}.".format(sum(abs_delta), sum(divisors)))