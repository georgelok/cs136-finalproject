# A skeleton of the greedy approximation algorithm of the WDP for CAs

import math
# Input bids: a set of (string, tuple, int) bids
# Output: a set of (string, tuple) bids consisting only of winners
def greedy(bids):
	values = []
	for owner, items, bid in bids:
		value = bid / math.sqrt(len(items))
		values.append((owner, set(items), value))

	# order bids by bid amount/sqrt(N), where N is number of items in package
	values.sort(key=lambda x: x[2], reverse=True)

	# output of winning bids
	winners = set([])

	#items that have already been allocated as part of winning bids
	allocated = set([])

	# Greedy algorithm, add package to winners 
	# if no atoms in package have been added yet
	for owner, items, value in values:
		found = False
		for item in items:
			if item in allocated:
				found = True
				break
		if found == False:
			winners.add((owner, tuple(items)))
			for item in items:
				allocated.add(item)

	print values
	print allocated
	return winners

test = set([])
test.add(("A", tuple(["a", "b"]), 7))
print test
test.add(("A", tuple(["d", "e"]), 8))
test.add(("B", tuple(["a", "c"]), 4))
print greedy(test)