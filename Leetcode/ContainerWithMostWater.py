def  max_area(height):
    compare = []
    compare[:] = list(set(sorted(height[:])))
    
    max_pos = height.index(compare[-1])
    pre_max = height.index(compare[-2])
    
    width_water = abs(max_pos - pre_max)

    return(width_water*compare[-2])

height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))