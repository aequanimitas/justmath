sample_space = [(x,y) for x in range(1,5,1) for y in range(1,5,1)]

sum_of_rolls_even = [x for x in sample_space if (x[0] + x[1]) % 2 == 0]
sum_of_rolls_odd = [x for x in sample_space if (x[0] + x[1]) % 2 != 0]
first_roll_equal_second = [x for x in sample_space if (x[0] == x[1])]
first_roll_larger_second = [x for x in sample_space if (x[0] > x[1])]
atleast_on_roll_equal_four = [x for x in sample_space if (x[0] == 4 or x[1] == 4)]

print sum_of_rolls_even
print sum_of_rolls_odd
print first_roll_equal_second
print first_roll_larger_second
print atleast_on_roll_equal_four
