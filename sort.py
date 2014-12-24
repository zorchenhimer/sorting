#!/usr/bin/python
"""
    Bogo Sort is best sort.
"""

import random
import time
import copy

def check_sort(lst):
	""" Check weather or not the given list is sorted. """
	last_item = None
	for item in lst:
		if last_item is None:
			last_item = item
		if item >= last_item:
			last_item = item
		else:
			return False
	return True

def BogoSort(unsorted):
	""" Preform a Bogo Sort on the given list and return a sorted list. """
	print('Starting sort')
	
	## Don't touch the original list.
	list_unsorted = copy.deepcopy(unsorted)
	
	## Number of itterations until we give up.
	itt = 1000000
	
	## Start the timer.
	time_start = time.time()
	
	list_sorted = []
	sort_done = False
	while not sort_done:
		## Clean the unsorted list, and recopy it.
		del list_unsorted[:]
		list_unsorted = copy.deepcopy(unsorted)
		
		## Clear the sorted list.
		del list_sorted[:]
		
		for i in range(len(list_unsorted)):
			## Pick a random item from the source list.
			idx = random.randint(0, len(list_unsorted) - 1)
			
			## Add it to the sorted list.
			list_sorted.append(list_unsorted[idx])
			
			## Remove the item from the source list.
			del list_unsorted[idx]
		
		if check_sort(list_sorted):
			## List is sorted.  We're done.
			sort_done = True
		elif itt > 0:
			## We didn't hit the itteration limit.  Try again.
			itt -= 1
		elif itt <= 0:
			## We hit the itteration limit.  Abort.
			sort_done = True
			print('Itteration limit hit! Aborting.')
	
	## Stop the timer.
	time_end = time.time()
	print('Sort finished.  Sorting {l} elements took {s} seconds.'.format(l=len(list_sorted), s=(time_end - time_start)))
	
	return list_sorted

## Construct an unsorted list of a given length.
unsorted_list = []
for i in range(8):
	unsorted_list.append(random.randint(1, 100))

## Do the thing.
print('List before sort: {l}'.format(l=unsorted_list))
sorted_list = BogoSort(unsorted_list)
print('List after sort: {l}'.format(l=sorted_list))