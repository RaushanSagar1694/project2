
# WAP to take a input and calculate fibonacchi number

def findFib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return findFib(n-1) + findFib(n-2)


num = int (input("Enter a number: "))
result = findFib(num)

print(result)



