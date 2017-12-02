import collections as co
import pprint as pr
#get puzzle imput from file
f = open("./day1_inp.txt", 'r')
inp_string = f.read()
f.close()

ilist = list(inp_string)
for i,x in enumerate(ilist): # converts srting elements into integers over the list
  ilist[i] = int(x)
idq = co.deque(ilist) #makes deque from the data
hits_part1 = list() # empty list for digits that fit the criteria
hits_part2 = list()
halfway = int((len(ilist)/2)) # defines the position halfway through the deque from item '0'

for i in range(len(ilist)): #Iterates a number of times equal to items in the list, BAD?
  if idq[0] == idq[1]:
    hits_part1.append(idq[0]) # if the item passes, add it to the list
  if idq[0] == idq[halfway]:
    hits_part2.append(idq[0])
  idq.rotate(-1)
  

pr.pprint('The solution to part 1 is {0}. The solution to part 2 is {1}.'.format(sum(hits_part1),sum(hits_part2)))