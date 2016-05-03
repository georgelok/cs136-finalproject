from parse import parse_2atom
from greedy import greedy
from twoatom import twoatom
import cplex
import time
import csv

num_goods = ['100', '500', '1000']
num_bids = ['100', '500', '1000', '2000', '4000']

greedy_results = []
twoatom_results = []
ibm_results = []

for bid in num_bids :
	for good in num_goods :
		print "testing 2-atom-"+good+"-"+bid
		for i in range(5) :
			test = parse_2atom('testfiles/2atom_nodomck/2atom-'+good+'-'+bid+'-000'+str(i)+'.txt')
			start = time.time()
			revenue = greedy(test[3], test[4])
			length = time.time() - start
			greedy_results.append([good, bid, revenue, length])

for bid in num_bids :
	for good in num_goods :
		print "testing 2-atom-"+good+"-"+bid
		for i in range(5) :
			test = parse_2atom('testfiles/2atom_nodomck/2atom-'+good+'-'+bid+'-000'+str(i)+'.txt')
			start = time.time()
			revenue = twoatom(test[3], test[4])
			length = time.time() - start
			twoatom_results.append([good, bid, revenue, length])

for bid in num_bids :
	print "\n\n\n\n\nstarting IBM BID: " + str(bid) + "\n\n\n\n\n"
	for good in num_goods :
		print "testing 2-atom-"+good+"-"+bid
		for i in range(5) :
			c = cplex.Cplex('testfiles/2atom_nodomck/2atom-'+good+'-'+bid+'-000'+str(i)+'.lp')
			# Parameters
			# Aggressive Probing
			# 5% away from optimal
			# Prioritize Feasible solutions
			c.parameters.mip.strategy.probe.set(3)
			c.parameters.mip.tolerances.mipgap.set(0.05)
			c.parameters.emphasis.mip.set(1)
			c.parameters.timelimit.set(300) 			
			start = time.time()
			c.solve()
			length = time.time() - start
			revenue = c.solution.get_objective_value()
			ibm_results.append([good, bid, revenue, length])

with open('resultfiles/2atom-greedy-nodomck.csv', 'wb') as f :
	wr = csv.writer(f)
	wr.writerows(greedy_results)

with open('resultfiles/2atom-twoatom-nodomck.csv', 'wb') as f :
	wr = csv.writer(f)
	wr.writerows(twoatom_results)

with open('resultfiles/2atom-ibm-nodomck.csv', 'wb') as f :
	wr = csv.writer(f)
	wr.writerows(ibm_results)

print greedy_results
print ibm_results
