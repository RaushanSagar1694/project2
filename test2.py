
# WAP TO FIND SPECIFIC SYMBOLE IN GIVEN STRING OR NOT

def find (str, value):
    
    for char in str:
        if char == value:
            return True
        
    return False   


str = "Raushan Sagar"
value = "h"

result = find(str, value)

print(result) 