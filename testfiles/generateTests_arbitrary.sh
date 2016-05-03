#!/bin/sh
for i in 100 500 1000
do
	for j in 100 500 1000 2000 4000
	do
		./cats -d arbitrary -goods $i -bids $j -filename arbitrary/arbitrary-$i-$j- -n 5 -cplex
	done
done