#!/bin/sh
for i in 100 500 1000
do
	for j in 100 500 1000 2000 4000
	do
		./cats -d arbitrary -goods $i -bids $j -filename 3atom/3atom-$i-$j- -n 5 -cplex -no_dom_check
	done
done