sample_space = [(x,y) for x in range(1,5,1) for y in range(1,5,1)]

sum_of_rolls_even = [x for x in sample_space if sum(x) % 2 == 0]
sum_of_rolls_odd = [x for x in sample_space if sum(x) % 2 != 0]
first_roll_equal_second = [x for x in sample_space if (x[0] == x[1])]
first_roll_larger_second = [x for x in sample_space if (x[0] > x[1])]
atleast_on_roll_equal_four = [x for x in sample_space if (x[0] == 4 or x[1] == 4)]

print sum_of_rolls_even
print sum_of_rolls_odd
print first_roll_equal_second
print first_roll_larger_second
print atleast_on_roll_equal_four

## using numpy
import numpy as np

x_labels = np.array("1 2 3 4".split())
# we need a reversed order array for y label
y_labels = np.array("1 2 3 4".split()[::-1])
two_d_grid = np.zeros((5,5), object)

## setup labels
## apply to fourth row (0), per column
two_d_grid[4,1:] = x_labels
## apply to first column, all rows
two_d_grid[:4,0] = y_labels
