import re
import sys

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokenNames = ["Duck_Honk", "Duck_Quack"]
        self.numOrSymbol = re.compile('(quack|honk)')
        self.tokens = []
        self.errors = []

    def lexer(self):
        self.tokenize = re.findall(self.numOrSymbol, self.text)
        for tok in self.tokenize:
            if tok == 'honk':
                self.tokens.append([tok, self.tokenNames[0]])
            elif tok == 'quack':
                self.tokens.append([tok, self.tokenNames[1]])
            else:
                self.errors.append(tok)
        if not self.errors:
            return self.tokens
        else:
            print("Error! Found unknown tokens.")
            print(self.errors)
            sys.exit()