# A skeleton of the greedy approximation algorithm of the WDP for CAs

import math
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

	print values
	print allocated
	print winners
	return revenue

b = [7, 8, 4]
a = [["a", "b"], ["d", "e"], ["a", "c"]]

print greedy(b, a)





