
# WAP to crate an object and make two function getString and upeer case


class Demo:
    
    def __init__ (self):
        self.str = ""
    
    def getString(self):
        self.str = str(input("Enter input : "))
    
    def printString(self):
        
        print("upper case is :", self.str.upper())    

obj = Demo()
obj.getString()
obj.printString()


            
        