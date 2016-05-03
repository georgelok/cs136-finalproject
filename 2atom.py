# An implementation of the optimization for 2-atom auctions

import numpy as np
from blossom import maxWeightMatching



def twoatom(bids, atoms):

	# Find the atoms and order them
	unique_atoms = set([])
	for atom_list in atoms:
		for atom in atom_list:
			unique_atoms.add(atom)
	unique_atoms = list(unique_atoms)
	

	max_bid = max(bids)

	unique_bids = {}

	edges = []

	for i in xrange(len(bids)):
		# Create a graph in which:
		# Each vertex corresponds to an atom
		# Each edge between two vertices corresponds to a bid
		# The weight corresponds to the bid value
		first = unique_atoms.index(atoms[i][0])
		second = unique_atoms.index(atoms[i][1])

		if (first, second) in unique_bids:
			if unique_bids[(first, second)] <  bids[i]:
				unique_bids[(first, second)] = bids[i]
		elif (second, first) in unique_bids:
			if unique_bids[(second, first)] < bids[i]:
				unique_bids[(second, first)] = bids[i]
		else:
			unique_bids[(first, second)] = bids[i]

	edges = [(i,j,v) for (i,j),v in unique_bids.iteritems()]
	
	print edges
	# Run the blossom algorithm for maximum weight matching on our graph
	mates = maxWeightMatching(edges)
	
	total_revenue = 0
	for i in xrange(len(mates)):
		if mates[i] == -1:
			continue
		else:
			mate = mates[i]
		if (mate, i) in unique_bids:
			total_revenue += unique_bids[(mate, i)]
	return total_revenue
	



