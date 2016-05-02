from parse import parse_3atom
from greedy import greedy
import cplex
import time
import csv

num_goods = ['100', '500', '1000']
num_bids = ['100', '500', '1000', '2000', '4000']

greedy_results = []
ibm_results = []

for bid in num_bids :
	for good in num_goods :
		print "testing 3-atom-"+good+"-"+bid
		for i in range(5) :
			test = parse_3atom('testfiles/3atom/3atom-'+good+'-'+bid+'-000'+str(i)+'.txt')
			start = time.time()
			revenue = greedy(test[3], test[4])
			length = time.time() - start
			greedy_results.append([good, bid, revenue, length])

for bid in num_bids :
	print "\n\n\n\n\nstarting IBM BID: " + str(bid) + "\n\n\n\n\n"
	for good in num_goods :
		print "testing 3-atom-"+good+"-"+bid
		for i in range(5) :
			c = cplex.Cplex('testfiles/3atom/3atom-'+good+'-'+bid+'-000'+str(i)+'.lp')
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

with open('resultfiles/3atom-greedy.csv', 'wb') as f :
	wr = csv.writer(f)
	wr.writerows(greedy_results)

with open('resultfiles/3atom-ibm.csv', 'wb') as f :
	wr = csv.writer(f)
	wr.writerows(ibm_results)

print greedy_results
print ibm_results
