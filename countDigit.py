
# wap to print to cout the number of digit 

def solve(num):
    result = 0
    num = str(abs(num))
    
    for n in num:
        if n.isdigit():
            result += 1
            
    return result

num = 324325676543456786543
result = solve(num)
print(result)
    