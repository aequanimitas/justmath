list_of_lists= [[1,2,3], [4,5,6], [7,8,9]]
easier_to_read_list_of_lists = [ [1,2,3], 
                                 [4,5,6], 
                                 [7,8,9] ]

two_plus_three = 2 + \
                 3

import re
my_regex = re.compile("[0-9]+", re.I)

# Strings
not_tab_string = r"\t"
print len(not_tab_string)

multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

# Exceptions
# in Python, there is no shame in using exceptions to make the code cleaner
try:
    print 0/0
except ZeroDivisionError:
    print "cannot divide by zero"

integer_list = [1,2,3]
heterogeneous_list =["Apple", 2, True]
list_mix = [ integer_list, heterogeneous_list ]

list_length = len(integer_list)
list_sum = sum(integer_list)

# negative indices


# range start number by default is 0
# range produces list with elements from 1 to 9
x_list = range(10)

# range with start value
xx_list = range(1, 10, 1)

# range produces list with elements from 1 to 9, with jumps
xy_list = range(1,10,2)

# "pythonic" for last element
xy_list[-1]

# slices
x_list_first_three = x_list[:3]
x_list_three_to_end = x_list[3:]
x_list_first_four = x_list[1:5]
x_list_last_three = x_list[-3:]
x_list_trim_frist_and_last = x_list[1:-1]
copy_x_list = x_list[:]

# the ```in``` operator. This checks elements in a list one by one
# can be used in tuples too
print 4 in range(10)
c_list = range(100)

# changes the original list
c_list.extend(range(10))

# no changes in original list
c_list_add = c_list + [1,2,3]

# unpacking lists
# throws error Too Many Values to Unpack if the count of variables on both sides doesn't
# match.
# use _ as a catcher for unwanted values

_,y = [1,2]

# Tuples
# lists immutable cousins
# useful if you want to return multiple values from a function
xx, yy = [1,2]
