-- Basic Types 

biggestInt, smallestInt :: Int
biggestInt = maxBound
smallestInt = minBound

-- integers
n :: Integer
n = 1234567890987654321987340982334987349872349874534

reallyBig :: Integer
reallyBig = 2^(2^(2^(2^2)))

-- Double
d1, d2 :: Double
d1 = 4.5387
d2 = 6.2831e-4

-- Booleans
b1, b2 :: Bool
b1 = True
b2 = False

-- Arithmetic
ex01 = 3 + 2
ex02 = 19 -27
ex03 = 2.35 * 8.6
ex04 = 8.7 / 3.1
ex05 = mod 19 3
ex06 = 19 `mod` 3
ex07 = 7 ^ 222
ex08 = (-8) * (-7)

ex09_01 = div 12 5
ex10 = 12 `div` 5

-- Boolean
ex11 = True && False
ex12 = not (False || True)

ex13 = 'a' == 'a'
