import re
import sys

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokenNames = ["Dog_Sad", "Dog_Talk"]
        self.numOrSymbol = re.compile('(u|woof)')
        self.tokens = []
        self.errors = []

    def lexer(self):
        self.tokenize = re.findall(self.numOrSymbol, self.text)
        for tok in self.tokenize:
            if tok == 'u':
                self.tokens.append([tok, self.tokenNames[0]])
            elif tok == 'woof':
                self.tokens.append([tok, self.tokenNames[1]])
            else:
                self.errors.append(tok)
        if not self.errors:
            return self.tokens
        else:
            print("Error! Found unknown tokens.")
            print(self.errors)
            sys.exit()