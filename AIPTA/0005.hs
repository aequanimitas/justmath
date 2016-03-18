import Data.List

example5ICEventAPred x = x !! 0 == "b" && x !! 1 == "b"
example5ICEventHPred x = "b" `elem` x
example5IC = [[x,y] | x <- ["b", "g"], y <- ["b", "g"]]

example5ICEventH = [x | x <- example5IC, example5ICEventHPred x]
example5ICEventA = [x | x <- example5IC, example5ICEventAPred x]
