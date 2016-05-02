# An implementation of the greedy approximation algorithm of the WDP for CAs

import math
from parse import parse

# Input bids: a list of floats; atoms: a list of lists of atoms
# Output: a set of (string, tuple) bids consisting only of winners
def greedy(bids, atoms):
	values = []
	for i in xrange(len(bids)):
		value = bids[i]/ math.sqrt(len(atoms[i]))
		values.append((i, value))

	# order bids by bid amount/sqrt(N), where N is number of items in package
	values.sort(key=lambda x: x[1], reverse=True)

	# output of winning bids
	revenue = 0

	# winning bids (for debugging)
	winners = []

	#items that have already been allocated as part of winning bids
	allocated = set([])

	# Greedy algorithm, add package to winners 
	# if no atoms in package have been added yet
	for i in xrange(len(values)):
		found = False
		for item in atoms[values[i][0]]:
			if item in allocated:
				found = True
				break
		if found == False:
			revenue += bids[values[i][0]]
			winners.append((bids[values[i][0]], atoms[values[i][0]]))
			for item in atoms[values[i][0]]:
				allocated.add(item)

	#print values
	#print allocated
	#print winners
	return revenue

#b = [7, 8, 4]
#a = [["a", "b"], ["d", "e"], ["a", "c"]]

#print greedy(b, a)

test0 = parse('testfiles/3atom-100-1000-0000.txt')
print "Revenue Testfile 0: " + str(greedy(test0[3], test0[4]))


test1 = parse('testfiles/3atom-100-1000-0001.txt')
print "Revenue Testfile 1: " + str(greedy(test1[3], test1[4]))

test2 = parse('testfiles/3atom-100-1000-0002.txt')
print "Revenue Testfile 2: " + str(greedy(test2[3], test2[4]))

test3 = parse('testfiles/3atom-100-1000-0003.txt')
print "Revenue Testfile 3: " + str(greedy(test3[3], test3[4]))

test4 = parse('testfiles/3atom-100-1000-0004.txt')
print "Revenue Testfile 4: " + str(greedy(test4[3], test4[4]))




