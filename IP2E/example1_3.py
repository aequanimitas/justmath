import operator

sample_space = [(x,y) for x in range(1,5,1) for y in range(1,5,1)]

def sumRollsEven(x, oper=None):
    if oper:
        return oper(sum(x) % 2 == 0)
    else:
        return sum(x) % 2 == 0

def firstRoll(x, comp=None):
    if comp:
        x,y = x
        return comp(x,y)
    else:
        return False

def generateEventSpace(lst, cond=None, oper=None):
    if cond:
        if oper:
            return [x for x in lst if cond(x, oper)]
        else:
            return [x for x in lst if cond(x)]
    else:
        return [x for x in lst]

sumOfRollsEven = generateEventSpace(sample_space, sumRollsEven)
sumOfRollsOdd = generateEventSpace(sample_space, sumRollsEven, operator.not_)
firstRollEqualSecond = generateEventSpace(sample_space, firstRoll, operator.eq)
firstRollLargerSecond = generateEventSpace(sample_space, firstRoll, operator.gt)
atleast_on_roll_equal_four = [x for x in sample_space if (x[0] == 4 or x[1] == 4)]

## using numpy
import numpy as np

# x_labels = np.array("1 2 3 4".split())
x_labels = y_labels = np.array(range(1,5,1))
# we need a reversed order array for y label
# y_labels = np.array("1 2 3 4".split()[::-1])
grid = np.zeros((5,5), object)

## setup labels
## apply to fourth row (0), per column
grid[4,1:] = x_labels
## apply to first column, all rows
grid[:4,0] = y_labels

## manual insertion of elements
grid[3,1:] = [(x, 1) for x in range(1,5,1)]
grid[2,1:] = [(x, 2) for x in range(1,5,1)]
grid[1,1:] = [(x, 3) for x in range(1,5,1)]
grid[0,1:] = [(x, 4) for x in range(1,5,1)]

## just list comprehension
np_sore = sorted([x for a in grid[:] for x in a if type(x) != int and sum(x) % 2 == 0]) == \
          sorted([v for i, v in np.ndenumerate(grid) if type(v) != int and sum(v) % 2 == 0]) == \
          sumOfRollsEven

# np_soro = [x for a in grid[:] for x in a if type(x) != int and sum(x) % 2 != 0]

## try by using pure numpy
