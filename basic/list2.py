#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
import time


def remove_adjacent(nums):
    # +++your code here+++
    if nums == []:
        return nums
    nums_copy = [nums[0]]

    i = 1
    while i < len(nums):
        if nums[i] != nums[i-1]:
            nums_copy.append(nums[i])
        i += 1

    return nums_copy


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    # +++your code here+++
    # look at the two sorted piles
    # compare each value
    # add the lower value to the third pile and increment the pile that we took from until both piles are empty
    start_time = time.time()
    list1_count = 0
    list2_count = 0
    sorted_List = []

    while list1_count < len(list1) and list2_count < len(list2):
        if list1[list1_count] < list2[list2_count]:
            sorted_List.append(list1[list1_count])
            list1_count += 1

        elif list1[list1_count] == list2[list2_count]:
            sorted_List.append(list1[list1_count])
            sorted_List.append(list2[list2_count])
            list2_count += 1
            list1_count += 1

        else:
            sorted_List.append(list2[list2_count])
            list2_count += 1

    if list1_count == len(list1):
        endtime = time.time()
        print(endtime - start_time)
        return sorted_List + list2[list2_count:]
    else:
        endtime = time.time()
        print(endtime - start_time)
        return sorted_List + list1[list1_count:]

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
    test(linear_merge(['aa', 'bb', 'cc'], ['aa', 'bb', 'cc']),
         ['aa', 'aa', 'bb', 'bb', 'cc', 'cc'])


if __name__ == '__main__':
    main()
