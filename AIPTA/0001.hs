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
sampleSpace = [
  ["abc","",""], 
  ["","abc",""], 
  ["","","abc"],
  ["ab","c",""], 
  ["ac","b",""], 
  ["bc","a",""], 
  ["ab","","c"], 
  ["ac","","b"], 
  ["bc","","a"], 
  ["a","bc",""], 
  ["b","ac",""], 
  ["c","ab",""], 
  ["a","","bc"], 
  ["b","","ac"], 
  ["c","","ab"], 
  ["","ab","c"], 
  ["","ac","b"], 
  ["","bc","a"], 
  ["","a","bc"], 
  ["","b","ac"], 
  ["","c","ab"],
  ["a","b","c"], 
  ["a","c","b"], 
  ["b","a","c"], 
  ["b","c","a"], 
  ["c","a","b"], 
  ["c","b","a"]]

charSet = ["a", "b", "c"]
-- sampling with replacement and with ordering
ssComprehension = [[x,y,z] | x <- charSet, y <- charSet, z <- charSet]

-- indistiguishableBalls = [
--   ["aaa","",""],
--   ["","aaa",""],
--   ["","","aaa"],
--   ["aa","a",""],
--   ["aa","","a"],
--   ["a","aa",""],
--   ["a","","aa"],
--   ["","aa","a"],
--   ["","a","aa"],
--   ["a","a","a"]
-- ]

generate4to9 = [[x,y,z] | x <- ["a", "aa", " "], y <- ["a", "aa", " "], z <- [" "]]

-- ibDistribution = [
--   1 % 27,
--   1 % 27,
--   1 % 27,
--   1 % 9,
--   1 % 9,
--   1 % 9,
--   1 % 9,
--   1 % 9,
--   1 % 9,
--   2 % 9
-- ]

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

-- discrete sample space
ex5A = [x / 27 :: Rational | x <- [1..length sampleSpace], x <- [1]]

factorial :: Integer -> Integer
factorial x
  | x == 0         = 0
  | (x - 1) == 0   = x
  | otherwise      = x * factorial (x - 1)

permute :: Integer -> Integer -> Integer
permute x y
  | x == 1         = 1 
  | y == 0         = permute x 1
  | x == y         = 1
  | otherwise      = x * permute (x - 1) y

ssc [] = [[]]

-- Exercises

-- 3
exer3 = permutations [1..4]
exer3A1 = [ x | x <- exer3, (x !! 0 < x !! 1) && (x !! 1 < x !! 2) && (x !! 2 < x !! 3)]
