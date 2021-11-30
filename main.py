from LA import Lexer
from SA import Parser
import pprint

equation = input("User input: ")
lexer = Lexer(equation)
tokens = lexer.lexer()
print("Lexical Analysis:")
pprint.pprint(tokens)
print("//-----------------------------------//")

print("Syntax Analysis:")
parser = Parser(tokens)
syntaxAnalysis = parser.parser()