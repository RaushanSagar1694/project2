

# WAP to take input and calculate avarage of the number


def avg (num1, num2, num3):
     sum = num1 + num2 + num3
     avgNum =  int (sum) / 3
     
     return avgNum
 
 
num1 = float (input("Enter input value"))
num2 = float (input("Enter input value"))
num3 = float (input("Enter input value"))

result = avg(num1, num2, num3)

print("Average of input value is:", result)


 
 