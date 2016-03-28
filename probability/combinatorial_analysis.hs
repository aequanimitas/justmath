-- 10 women, 3 children each
motherBoy = [(x,y) | x <- [1..10], y <- [1..3]]

commitee = [(x,y,z,a) | x <- [1..3], y <- [1..4], z <- [1..5], a <- [1,2]]

phPlakas = [(x,y,z,a,b,c,d) | x <- ['A'..'Z'], y <- ['A'..'Z'], z <- ['A'..'Z'], a <- [0..9], b <- [0..9], c <- [0..9], d <- [0..9]]

