sample_space = [(x,y) for x in range(1,5,1) for y in range(1,5,1)]

sum_of_rolls_even = [x for x in sample_space if (x[0] + x[1]) % 2 == 0]
sum_of_rolls_odd = [x for x in sample_space if (x[0] + x[1]) % 2 != 0]
