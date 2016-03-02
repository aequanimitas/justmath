addVector :: [Int] -> [Int] -> [Int]
addVector [] [] = [0,0] -- zero vector
addVector x y = head(x) + head(y) : []
