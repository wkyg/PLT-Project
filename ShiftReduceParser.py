# Start Symbol:
# <Dog_Talk>
# <Dog_Sad> 

# Terminal Symbol:
# {u,woof}

# Production Rules: 
# <Dog_Talk>    -> woof
# <Dog_Sad> 	-> u
# <Dog_Scare>   -> <Dog_Talk> <Dog_Sad> woof u
# <Dog_Happy>	-> <Dog_Scare> <Dog_Talk> woof u woof
# <Dog_Angry>   -> <Dog_Talk> <Dog_Talk> woof woof


import sys

class Parser:
    
    def __init__(self, text):
        self.text = text
        self.stack = []
        self.a = ""
        self.action = "SHIFT"
        self.stackString = ""
        self.inputElement = 0
        self.ac = "REDUCE TO EXP -> "
        self.stacklength = len(self.stack)

    def popandstuff(self, x):
        for i in range(x):
            self.stack.pop()
            #print("\n")
            #print("stackstring",self.stackString)
            if(self.stackString == 'woof'):
                self.stack.append("<Dog_Talk>")

            elif(self.stackString == 'u'):
                self.stack.append("<Dog_Sad>")

            elif(self.stackString == '<Dog_Talk>u'):
                self.stack.pop()
                self.stack.append("<Dog_Scare>")

            elif(self.stackString == '<Dog_Scare>woof'):
                self.stack.pop()
                self.stack.append("<Dog_Happy>")
                
            elif(self.stackString == '<Dog_Talk>woof'):
                self.stack.pop()
                self.stack.append("<Dog_Angry>")            
            else :
                print("Reject")
                print("Syntax Analysis complete. The dog is confuse")
                quit()
                self.stack.clear()
                
        self.stackString = ""
        for i in range(len(self.stack)):
            self.stackString = self.stackString + self.stack[i]
        print("$" + self.stackString + "\t" + self.a + "$" + "\t", end='')
        # print("\n")
        # print("stack",self.stack)

    def number(self):
            self.stacklength = len(self.stack)
            if self.stack[self.stacklength - 1] == "woof":
                print(self.ac + "<Dog_Talk>")
                self.popandstuff(1)
            elif self.stack[self.stacklength - 1] == "u" : 
                print(self.ac + "<Dog_Sad>")
                self.popandstuff(1)            
            
    def twopart(self, first, last):
        self.stacklength = len(self.stack)
        if self.stacklength > 2 and self.stack[self.stacklength - 1] == last:
            if self.stack[self.stacklength - 2] == first:
                if self.stack[self.stacklength - 3] != "<EXP>":
                    print(self.ac + first + last)
                    self.popandstuff(2)
        elif self.stacklength > 1 and self.stack[self.stacklength - 1] == last:
            if self.stack[self.stacklength - 2] == first:
                print(self.ac + first + last)
                self.popandstuff(2)
       
    def threepart(self, first, middle, last):
        self.stacklength = len(self.stack)
        if self.stacklength > 2 and self.stack[self.stacklength - 1] == last:
            if self.stack[self.stacklength - 2] == middle:
                if self.stack[self.stacklength - 3] == first:
                    print(self.ac + first + middle + last)
                    self.popandstuff(3)

    def checkrules(self):
        self.number()
        self.twopart("<Dog_Talk>","<Dog_Sad>")
        self.twopart("<Dog_Scare>","<Dog_Talk>")        
        # self.twopart("<Dog_Talk>","<Dog_Scare>")
        # self.twopart("woof","woof")

    def checkvalid(self):
        self.stacklength = len(self.stack)
        if (self.stacklength == 1 and self.stack[self.stacklength - 1] == "<Dog_Talk>"):
            print("Accept")
            print("Syntax Analysis complete. The dog is talking.")
        elif (self.stacklength == 1 and self.stack[self.stacklength - 1] == "<Dog_Sad>"):
            print("Accept")
            print("Syntax Analysis complete. The dog is sad.")
        elif (self.stack[self.stacklength - 1] == "<Dog_Scare>"):
            print("Accept")
            print("Syntax Analysis complete. The dog is scare.")
        elif (self.stack[self.stacklength - 1] == "<Dog_Happy>"):
            print("Accept")
            print("Syntax Analysis complete. The dog is happy.")
        elif (self.stack[self.stacklength - 1] == "<Dog_Angry>"):
            print("Accept")
            print("Syntax Analysis complete. The dog is angry.")        
        else:
            print("ending",self.stack[self.stacklength - 1])
            print("Reject")
            print("Syntax Analysis complete. The dog is confuse")
            sys.exit()

    def maincheck(self):
        for x in range(len(self.text)):
            # Reset variables
            self.a = ""
            self.stackString = ""

            # Print action
            print(self.action)

            # Pushing into stack
            if (self.text != ""):
                self.stack.append(self.text[x][0])
            # Make all the elements in the stack a string
            # so that it is easier to print
            for i in range(len(self.stack)):
                self.stackString = self.stackString + self.stack[i]

            # Move forward the pointer for the input string
            self.inputElement = self.inputElement + 1
            # Make all the elements in the the input array a
            # string so that it is easier to print
            for i in range(len(self.text) - self.inputElement):
                self.a = self.a + self.text[i + self.inputElement][0]

            # Print stack and input
            print("$" + self.stackString + "\t" + self.a + "$" + "\t", end='')

            self.checkrules()

    def parser(self):
        for x in range(len(self.text) - self.inputElement):
            self.a = self.a + self.text[x + self.inputElement][0]
        print("stack \t input \t action")
        print("$ \t" + self.a + "$" + "\t", end='')

        # Main function for shift reduce parser
        self.maincheck()

        # Check for production rules one last time
        self.checkrules()

        # Check if syntax is correct or not
        self.checkvalid()


            



