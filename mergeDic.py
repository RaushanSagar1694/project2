
# WAP to merge to dictionary 

def mergeTwoDic(dis1, dis2):
    temp = dis1.copy()
    temp.update(dis2)
    
    return temp

dis1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
dis2 = {'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}

result = mergeTwoDic(dis1, dis2)
print(result)