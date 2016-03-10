addVector :: [Int] -> [Int] -> [Int]
addVector x y
  | length x == 1 && length y == 1  = [head(x) + head(y)]
  | otherwise                       = head(x) + head(y) : addVector (drop 1 x) (drop 1 y)

-- via list comprehension
addVectorLC x y = [[a,b] | a <- (x !! 0 + y !! 0), b <- (x !! 1 + y !! 1)]
