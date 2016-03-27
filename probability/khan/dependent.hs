import Data.List

urn = ["g","g","g","o","o"]

g s = map (\x->(head x, length x)) . group . sort $ s

prob1stGreen = fromIntegral ( snd(head (g urn))) / fromIntegral (length urn) :: Rational

picked1stGreen = delete "g" urn

prob2ndGreen = fromIntegral (snd (head (g picked1stGreen))) / fromIntegral (length picked1stGreen) :: Rational
