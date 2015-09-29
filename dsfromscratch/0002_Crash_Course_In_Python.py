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
