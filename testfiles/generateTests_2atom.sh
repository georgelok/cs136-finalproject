#!/bin/sh
for i in 100 500 1000
do
	for j in 100 500 1000 2000 4000
	do
		./cats -d L3 -goods $i -bids $j -filename 2atom/2atom-$i-$j- -n 5 -cplex -const_goods 2
	done
done