import Data.List
-- sum six
dieRoll x = [1..x]

sumSix = [[x,y] | x <- dieRoll 6, y <- dieRoll 6, x + y == 6]
twoOddFace = [[x,y]| x <- dieRoll 6, y <- dieRoll 6, odd x && odd y]


-- relation among events

relUnion = [1..5] `union` [6..10]
relIntersection = [1..10] `intersect` [5..15]
relNotIn = ([1..10] \\ [1..5])
occImpliesNonOcc = length([1..10] \\ [1..5])

-- husband and wife example
predicateA x = x > 40
predicateB x y = x > y
predicateC x y = x > 40 && y = 40

-- apply predicate functions
