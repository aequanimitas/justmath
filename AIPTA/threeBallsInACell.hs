sampleSpace = [["abc","",""], ["","abc",""], ["","","abc"],["ab","c",""], ["ac","b",""], ["bc","a",""], ["ab","","c"], ["ac","","b"], ["bc","","a"], ["a","bc",""], ["b","ac",""], ["c","ab",""], ["a","","bc"], ["b","","ac"], ["c","","ab"], ["","ab","c"], ["","ac","b"], ["","bc","a"], ["","a","bc"], ["","b","ac"], ["","c","ab"],["a","b","c"], ["a","c","b"], ["b","a","c"], ["b","c","a"], ["c","a","b"], ["c","b","a"]]

-- should be 21
eventAPredicate x = length x >= 2
eventA = [x | x <- sampleSpace, any eventAPredicate x]

eventBPredicate x = length(x !! 0) > 0
eventB = [x | x <- sampleSpace, eventBPredicate x]

eventCPredicate x = (eventBPredicate x) && (eventAPredicate x)
eventC = [x | x <- sampleSpace, eventBPredicate x, eventAPredicate x]
