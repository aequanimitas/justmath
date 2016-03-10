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
predicateC x y = x > 40 && y >= 40

-- relation among events
--
sampleSpace = [["abc","",""], ["","abc",""], ["","","abc"],["ab","c",""], ["ac","b",""], ["bc","a",""], ["ab","","c"], ["ac","","b"], ["bc","","a"], ["a","bc",""], ["b","ac",""], ["c","ab",""], ["a","","bc"], ["b","","ac"], ["c","","ab"], ["","ab","c"], ["","ac","b"], ["","bc","a"], ["","a","bc"], ["","b","ac"], ["","c","ab"],["a","b","c"], ["a","c","b"], ["b","a","c"], ["b","c","a"], ["c","a","b"], ["c","b","a"]]

cellLength x y = length x == y
-- E1E2 = T3
exDef4Fn a b = [x | x <- sampleSpace , cellLength (x !! a) b]
e1Empty = exDef4Fn 0 0
e2Empty = exDef4Fn 1 0

triply3 = exDef4Fn 2 3
triply1 = exDef4Fn 0 3

simply3 = exDef4Fn 2 1
simply2 = exDef4Fn 1 1
simply1 = exDef4Fn 0 1

s1s2ImpliesS3 = [x | x <- simply1 `intersect` simply2, x `elem` simply3]

doubly1 = exDef4Fn 0 2
doubly2 = exDef4Fn 1 2
doubly3 = exDef4Fn 2 2

-- if cell 1 length is greater than 0
-- and if cell 2 length is greater than 0
-- then an empty event happens
d1d2Empty = length (doubly1 `intersect` doubly2) == 0

t3ImpliesE2 = [x | x <- triply1, x `elem` e2Empty]

dUnion = doubly1 `union` doubly2 `union` doubly3