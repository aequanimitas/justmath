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

# can also be used in multiple assignment
xxx, yyy = (1,2)

# swapping variables
xxx, yyy = yyy, xxx

# dictionaries
tweet = {
        "user": "joelgrus",
        "text" : "Data Science is Awesome",
        "retweet_count" : 100,
        "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
        }

tweet_keys = tweet.keys()
tweet_items = tweet.items()
tweet_values = tweet.values()

## using ```in``` in a list is slow
"user" in tweet_keys

## while in dictionaries, it is much faster
"user" in tweet

# using defaultdict
# useful when you're trying to count frequency
# you do not need to worry if a key in the dictionary exists as it will be handled
# gracefully
# it also adds a value on the object if a key is not in the dictionary using the
# zero-argument function you provided when it is created

from collections import defaultdict

document = "Every one of these is slightly unwieldy, which is why defaultdict is useful. \
A defaultdict is like a regular dictionary, except that when you try to look up a key it \
doesn't contain, it first adds a value for it using a zero-argument function you provided"

# the ```int``` argument says it defaults to 0
word_count = defaultdict(int)
for word in document.split():
    word_count[word] += 1
   
# while a Counter turns a sequence into a defaultdict-like object mapping keys to counts
from collections import Counter
word_count_counter = Counter(document.split())

# most common
word_count_counter.most_common(10)

# Sets: A collection of distinct elements
s = set()
s.add(1)
s.add(1)

# you can stack them!
set(list(range(10))) 

# Boolean
# this will return false but all values are "Falsy"
print False == None == [] == {} == "" == set() == 0 == 0.00

# use ```all``` to assert "Falsy"-ness
print all([False , None , [] , {} , "" , set() , 0 , 0.00])

## The not so basics
## sorting
## defaults to sorting smallest to biggest
pos_neg = range(-10,10)

## pos_neg.sort()
## to assign on new variable, use sorted: y = sorted(x)

## reverse
## the key is a key
sorted(pos_neg, key=abs, reverse=True)

## List Comprehensions
## use _ if you do not want to use some values
## you can use dictionaries too!
dct = {x: x + 1 for x in range(-10,10)}

## generators
## used when we need an object one element at a time, hindi isang bagsak
## always use a break logic, or it will continue to iterate forever

def natural_numbers():
    n = 0
    while n < 10:
        yield n
        n += 1

## use next() instead of the generator object method obj.next() to avoid the stop
## iteration error. the None argument means just return nothing
## if you assign the natural_numbers function into a new variable, it will return a new
## generator object starting from scratch

ggg = natural_numbers()

## on lists, instead of items(), using iteritems() will lazily build the key-value pairs

## Randomness
import random

four_uniform_randoms = [random.random() for _ in range(4)]

lasenggo = random.choice(["Dhen", "Jorj", "Tophe"])

## get a sample
lottery_numbers = range(1,73)
winning_numbers = random.sample(lottery_numbers, 6)

## regular expressions
import re
print all([
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3 == len(re.split("[ab]", "carbs")),
    "R-D-" == re.sub("[0-9]", "-", "R2D2")
    ])

## OOP
## recreating the Set class

class MySet:

    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """ This is helpful while in repl """
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        try:
            del self.dict[value]
        except KeyError:
            print "Key doesn't exist"

## Functional Tools
## currying
from functools import partial

## interesting way of using partials
## http://www.pydanny.com/python-partials-are-fun.html 

import string

alphaNumericTuples = zip(range(1,len(string.ascii_letters)), string.ascii_letters)

## args and kwargs

def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

def magic(*args, **kwargs):
    print "unnamed args: ", args
    print "keyword args: ", kwargs
