#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
	r is a reader
	returns an generator that iterates over a sequence of lists of ints of length 2
	for s in r :
	l = s.split()
	b = int(l[0])
	e = int(l[1])
	yield [b, e]
	"""
    return (map(int, s.split()) for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval ((i, j)) :
    """
	i is the beginning of the range, inclusive
	j is the end of the range, inclusive
	return the max cycle length in the range [i, j]
	"""
    #-1 implies that cache has not been written to for this number
    cache = [-1] * 1000000
    #error checking; switch i and j if range is invalid
    if (i > j):
        iTemp = i
        i = j
        j = iTemp
    #Quiz 3 optimization
    m = j / 2
    if (i < m):
        i = m
    maxCycleLength = 1
    for number in range(i, j + 1):
        if (number < len(cache) and cache[number] != -1):
            numberCycleLength = cache[number]
        else:
            numberCycleLength = collatz_single(number, cache)
            if (number < len(cache)):
                cache[number] = numberCycleLength
        if (numberCycleLength > maxCycleLength):
            maxCycleLength = numberCycleLength
    return maxCycleLength

# --------------
# collatz_single
# --------------
def collatz_single (number, cache):
    """
    number is from the collatz_eval loop
    evaluates the cylces for a single number
    """
    cycles = 1
    while (number > 1):
        if (number < len(cache) and cache[number] != -1):
            return cycles + cache[number] - 1
        cycles += 1
        if (number % 2 == 1):
            number = (3 * number) + 1
        else:
            number = (number / 2)
    return cycles

	
# -------------
# collatz_print
# -------------

def collatz_print (w, (i, j), v) :
    """
	prints the values of i, j, and v
	w is a writer
	v is the max cycle length
	i is the beginning of the range, inclusive
	j is the end of the range, inclusive
	"""
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
	read, eval, print loop
	r is a reader
	w is a writer
	"""
    for t in collatz_read(r) :
        v = collatz_eval(t)
        collatz_print(w, t, v)
