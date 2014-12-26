#!/usr/bin/python

import time
import random
from multiprocessing  import Process, Queue

def sleeper(num, queue):
	time.sleep(num/1.6)
	queue.put(num)

def SleepSort(unsorted_list):
	process_list = []
	q = Queue()
	for item in unsorted_list:
		p = Process(target=sleeper, args=(int(item), q))
		p.start()
		process_list.append(p)
	
	while q.qsize() < len(process_list):
		pass
	
	q.put(None)
	
	sorted_list = []
	item = q.get()
	while item:
		sorted_list.append(item)
		item = q.get()
	
	return sorted_list
	
if __name__ == '__main__':
	lst = []
	for n in range(10):
		lst.append(random.randint(1, 10))

	print 'Before sort: {l}'.format(l=lst)
	sorted_lst = SleepSort(lst)
	print 'Done: {l}'.format(l=sorted_lst)