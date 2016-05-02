# An implementation of the optimization for 2-atom auctions

from parse import parse
import numpy as np

def twoatom(bids, atoms):
	# Find the atoms and order them
	unique_atoms = set([])
	for atom_list in atoms:
		for atom in atom_list:
			unique_atoms.add(atom)
	unique_atoms = list(unique_atoms)
	print unique_atoms

	max_bid = max(bids)

	# Create weight matrix of two-item bids,
	# Adding fake vertices for single-item bids
	Adj_matrix - np.matrix([[np.finfo(float).max for i in xrange(len(unique_atoms))] for j in xrange(len(unique_atoms))])

	for i in xrange(len(bids)):
		# Update weights if we find a better weight for this pair of edges
		if len(atoms[i]) == 2:
			first = unique_atoms.index(atoms[i][0])
			second = unique_atoms.index(atoms[i][1])
			if max_bids - bids[i] < Adj_matrix[first, second]:
				Adj_matrix[first, second] = max_bid - bids[i]
				Adj_matrix[second, first] = max_bid - bids[i]

		# Diagonal can consist of maximal single bids
		elif len(atoms[i]) == 1:
			first = unique_atoms.index(atoms[i][0])
			if max_bids - bids[i] < Adj_matrix[first, first]:
				Adj_matrix[first, first] = max_bid - bids[i]
				#Adj_matrix[len(unique_atoms + first - 1), first] = max_bid - bids[i]

	# Run the Hungarian algorithm
	rowmins = np.amin(Adj_matrix, axis=1)
	mins = np.repeat(rowmins, len(Adj_matrix), axis=1)
	step_one = np.subtract(Adj_matrix, mins)

	colmins = np.amin(step_one, axis=0)
	mins = np.repeat(colmins, len(step_one), axis=0)
	step_two = np.subtract(step_one, mins)

	assign = set([])
	cross = set([])
	rows_unassigned = set([])
	
	# Matrix is symmetric, so this is guaranteed to find a matching
	for i in xrange(len(unique_atoms)):
		assigned = False
		for j in xrange(len(unique_atoms)):
			if step_two[i, j] == 0 and (i, j) not in cross:
				if(i != j):
					if (j, i) not in assign:
						assign.add((i,j))
					assigned = True
					# Possible indices issue here
					for k in range(i+1,len(unique_atoms)):
						if step_two[k, j] == 0:
							cross.add((k, j))
		if not assigned:
			if step_two[i, i] == 0:
				assign.add((i,i))
				for k in range(i+1,len(unique_atoms)):
					if step_two[k, i] == 0:
						cross.add((k, i))
			else:
				rows_unassigned.add(i)

	print len(assign), len(unique_atoms)

	total_revenue = 0
	for x, y in assign:
		indices = []
		if(x == y):
			indices = [i for i, k in enumerate(atoms) if k == [x]]
		else:
			indices = [i for i, k in enumerate(atoms) if k == [x, y]]
			indices += [i for i, k in enumerate(atoms) if k == [y, x]]
		revenue = 0
		for index in indices:
			if bids[index] > revenue:
				revenue = bids[index]
		total_revenue += revenue

	return total_revenue





