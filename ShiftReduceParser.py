# Start Symbol:
# <Duck_Quack>
# <Duck_Honk>

# Terminal Symbol:
# {quack,honk}

# Production Rules: 
# <Duck_Quack>  -> quack
# <Duck_Honk>   -> honk
# <Duck_Curious>   -> <Duck_Quack> <Duck_Honk> example: quack honk
# <Duck_Happy>	-> <Duck_Curious> <Dog_Quack> quack honk quack
# <Duck_Angry>   -> <Duck_Honk> <Duck_Honk> honk honk


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
            if(self.stackString == 'quack'):
                self.stack.append("<Duck_Quack>")

            elif(self.stackString == 'honk'):
                self.stack.append("<Duck_Honk>")

            elif(self.stackString == '<Duck_Quack>honk'):
                self.stack.pop()
                self.stack.append("<Duck_Curious>")

            elif(self.stackString == '<Dog_Curious>quack'):
                self.stack.pop()
                self.stack.append("<Duck_Happy>")
                
            elif(self.stackString == '<Duck_Honk>honk'):
                self.stack.pop()
                self.stack.append("<Duck_Angry>")
            else :
                print("Reject")
                print("Syntax Analysis complete. The duck does not understand anything u just said")
                quit()
                self.stack.clear()
                
        self.stackString = ""
        for i in range(len(self.stack)):
            self.stackString = self.stackString + self.stack[i]
        print("$" + self.stackString + "\t\t\t" + self.a + "$" + "\t\t\t", end='')
        # print("\n")
        # print("stack",self.stack)

    def number(self):
            self.stacklength = len(self.stack)
            if self.stack[self.stacklength - 1] == "quack":
                print(self.ac + "<Duck_Quack>")
                self.popandstuff(1)
            elif self.stack[self.stacklength - 1] == "honk":
                print(self.ac + "<Duck_Honk>")
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
        self.twopart("<Duck_Quack>","<Duck_Honk>")
        self.twopart("<Duck_Honk>","<Duck_Quack>")

    def checkvalid(self):
        self.stacklength = len(self.stack)
        if (self.stacklength == 1 and self.stack[self.stacklength - 1] == "<Duck_Quack>"):
            print("Accept")
            print("Syntax Analysis complete. The duck is quacking.")
        elif (self.stacklength == 1 and self.stack[self.stacklength - 1] == "<Duck_Honk>"):
            print("Accept")
            print("Syntax Analysis complete. The duck is honking.")
        elif (self.stack[self.stacklength - 1] == "<Duck_Curious>"):
            print("Accept")
            print("Syntax Analysis complete. The duck is curious.")
        elif (self.stack[self.stacklength - 1] == "<Duck_Happy>"):
            print("Accept")
            print("Syntax Analysis complete. The duck is happy.")
        elif (self.stack[self.stacklength - 1] == "<Duck_Angry>"):
            print("Accept")
            print("Syntax Analysis complete. The duck is angry.")
        else:
            print("ending",self.stack[self.stacklength - 1])
            print("Reject")
            print("Syntax Analysis complete. The duck does not understand anything u just said")
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
            print("$" + self.stackString + "\t\t\t" + self.a + "$" + "\t\t\t", end='')

            self.checkrules()

    def parser(self):
        for x in range(len(self.text) - self.inputElement):
            self.a = self.a + self.text[x + self.inputElement][0]
        print("stack \t\t\t input \t\t\t action")
        print("$" + self.a + "$" + "\t\t\t", end='')

        # Main function for shift reduce parser
        self.maincheck()

        # Check for production rules one last time
        self.checkrules()

        # Check if syntax is correct or not
        self.checkvalid()


            



