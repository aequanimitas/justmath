addVector :: [Int] -> [Int] -> [Int]
addVector x y
  | length x == 1 && length y == 1  = [head(x) + head(y)]
  | otherwise                       = head(x) + head(y) : addVector (drop 1 x) (drop 1 y)
