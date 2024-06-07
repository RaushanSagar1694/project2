
# WAP to crate an object and make two function getString and upeer case


class Demo:
    
    def __init__ (self):
        self.str = ""
    
    def getString(self):
        self.str = str(input("Enter input : "))
    
    def printString(self):
        self.str = self.str.upper()
        
        print("upper case is :", self.str)    

obj = Demo()
obj.getString()
obj.printString()


            
        