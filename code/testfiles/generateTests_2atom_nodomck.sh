#!/bin/sh
for i in 100 500 1000
do
	for j in 100 500 1000 2000 4000
	do
		./cats -d L3 -goods $i -bids $j -filename 2atom_nodomck/2atom-$i-$j- -n 5 -cplex -const_goods 2 -no_dom_check -int_prices
	done
done