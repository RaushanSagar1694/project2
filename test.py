
def removeCharacter(str):
    result =""
    
    for char in str:
          
        if char.isdigit():
            result += char
            
    return result


str = "Jsaa1694 Hello1345"
result = removeCharacter(str)
print(result)
            