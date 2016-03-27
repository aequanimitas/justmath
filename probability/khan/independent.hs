-- two dice
twoDieRolls = [(x,y) | x <- [1..6], y <- [1..6]]

rollingDoublesPred x = (fst x) == (snd x) 

rollingDoubles =  [x | x <- twoDieRolls , rollingDoublesPred x]
