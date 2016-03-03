-- sum six
dieRoll x = [1..x]

sumSix = [[x,y] | x <- dieRoll 6, y <- dieRoll 6, x + y == 6]
twoOddFace = [[x,y]| x <- dieRoll 6, y <- dieRoll 6, odd x && odd y]
