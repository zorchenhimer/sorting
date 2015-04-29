#!/usr/bin/python

import random
import time

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

def BozoSort(unsorted):
    """ Preform a Bozo Sort on the given list and return a sorted list. """    
    ## Number of itterations until we give up.
    itt = 10000000

    ## Start the timer.
    time_start = time.time()

    sort_done = False
    tries = 0
    while not sort_done:
        tries += 1

        # Find to elements in the list.
        rand_idxA = random.randint(0, len(unsorted) - 1)
        rand_idxB = random.randint(0, len(unsorted) - 1)
        while rand_idxA == rand_idxB:
            rand_idxB = random.randint(0, len(unsorted) - 1)

        # Swap them.
        tmp = unsorted[rand_idxA]
        unsorted[rand_idxA] = unsorted[rand_idxB]
        unsorted[rand_idxB] = tmp

        if check_sort(unsorted):
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

    return (unsorted, tries)

def TimeSort(length, itterations):
    """ Gather statistics on running BozoSort for different list lengths. """
    stats = {
        'itterations':    itterations,
        'longest':        0,
        'shortest':        None,
        'average':        0,
        'fewest':        None,    ## Fewest tries
        'most':            0,        ## Most tries
        'all_times':    []
    }

    print('Starting TimeSort() with length of [{l}] for [{i}] itterations'.format(l=length, i=itterations))
    for i in range(itterations):
        if ((i + 1) % 10) == 0:
            print('Itteration {n}/{t}'.format(n=(i+1), t=itterations))
        ## Construct an unsorted list of a given length.
        unsorted_list = []
        for i in range(length):
            ## Do the thing
            unsorted_list.append(random.randint(1, 1000))

        start_time = time.time()
        (sorted_list, tries) = BozoSort(unsorted_list)
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
    for i in range(2, 11):
        stats = TimeSort(i, 400)
        total_time = 0
        total_tries = 0
        for data in stats['all_times']:
            total_time += data['time']
            total_tries += data['tries']

        avg_time = total_time / (stats['itterations'] * 1.0)
        avg_tries = total_tries / (stats['itterations'] * 1.0)

        fewest = stats['fewest']
        if fewest is None:
            fewest = 0

        print(
            "====\nTotal Time: {t}\nItterations: {i}\nLongest: {l}\nShortest: {s}\nAverage: {a}\nTotal Tries: {ttry}\nAverage Tries: {atry}\nMost: {m}\nFewest: {f}".format(
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
        f = open('data_{l}.csv'.format(l=i), 'w')
        #print('== Individual Itterations ==')
        for data in stats['all_times']:
            #print("{n:,} tries in {t:.2} seconds".format(n=data['tries'], t=data['time']))
            f.write("{n},{t}\n".format(n=data['tries'], t=data['time']))
        f.close()
