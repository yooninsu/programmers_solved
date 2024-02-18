def destination(map,plan):
    start = [1,1]
    for a in plan:
        if a == "L":
            start = [start[0],start[1]-1]
            if start[0] > map:
                start= [start[0],start[1]+1]
        if a == "R":
            start = [start[0],start[1]+1]
            if start[0] < 1:
                start= [start[0],start[1]-1]
        if a == "U":
            start = [start[0]-1,start[1]]
            if start[0] < 1:
                start= [start[0] + 1,start[1]]  
        if a == "D":
            start = [start[0]+1,start[1]]
            if start[0] > map:
                start= [start[0] -1,start[1]]
    print(start)

destination(5,["R","R","R","U",'D','D'])
        
