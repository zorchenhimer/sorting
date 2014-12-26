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
	## Don't touch the original list.
	list_unsorted = copy.deepcopy(unsorted)
	
	## Number of itterations until we give up.
	itt = 1000000
	
	## Start the timer.
	time_start = time.time()
	
	list_sorted = []
	sort_done = False
	tries = 0
	while not sort_done:
		tries += 1
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
	#print('Sort finished.  Sorting {l} elements took {s} seconds.'.format(l=len(list_sorted), s=(time_end - time_start)))
	
	return (list_sorted, tries)

def TimeSort(length, itterations):
	""" Gather statistics on running BogoSort for different list lengths. """
	stats = {
		'itterations':	itterations,
		'longest':		0,
		'shortest':		None,
		'average':		0,
		'fewest':		None,	## Fewest tries
		'most':			0,		## Most tries
		'all_times':	[]
	}
	
	print('Starting TimeSort() with length of [{l}] for [{i}] itterations'.format(l=length, i=itterations))
	for i in range(itterations):
		print('Itteration {n}/{t}'.format(n=(i+1), t=itterations))
		## Construct an unsorted list of a given length.
		unsorted_list = []
		for i in range(length):
			## Do the thing
			unsorted_list.append(random.randint(1, 1000))
		
		start_time = time.time()
		(sorted_list, tries) = BogoSort(unsorted_list)
		total_time = time.time() - start_time
		
		stats['all_times'].append({'time': total_time, 'tries': tries})
		
		if stats['longest'] < total_time:
			stats['longest'] = total_time
		
		if stats['shortest'] is None:
			stats['shortest'] = total_time
		elif stats['shortest'] > total_time:
			stats['shortest'] = total_time
		
		if stats['fewest'] is None:
			stats['fewest'] = tries
		elif stats['fewest'] > tries:
			stats['fewest'] = tries
		
		if stats['most'] < tries:
			stats['most'] = tries
		
	return stats
		
if __name__ == '__main__':
	## Do the thing.
	stats = TimeSort(8, 20)
	total_time = 0
	total_tries = 0
	for data in stats['all_times']:
		total_time += data['time']
		total_tries += data['tries']
	
	avg_time = total_time / (stats['itterations'] * 1.0)
	avg_tries = total_tries / (stats['itterations'] * 1.0)
		
	print(
		"====\nTotal Time: {t:.2}\nItterations: {i}\nLongest: {l:.2}\nShortest: {s:.2}\nAverage: {a:.2}\nTotal Tries: {ttry:,}\nAverage Tries: {atry:,}\nMost: {m:,}\nFewest: {f:,}".format(
			t = total_time,
			i = stats['itterations'],
			l = stats['longest'],
			s = stats['shortest'],
			a = avg_time,
			ttry = total_tries,
			atry = avg_tries,
			m = stats['most'],
			f = stats['fewest']
		)
	)
	print('== Individual Itterations ==')
	for data in stats['all_times']:
		print("{n:,} tries in {t:.2} seconds".format(n=data['tries'], t=data['time']))