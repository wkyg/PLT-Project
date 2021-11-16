from LexicalAnalyzer import Lexer
from ShiftReduceParser import Parser
import pprint


equation = input("User input: ")
lexer = Lexer(equation)
tokens = lexer.lexer()
print("LEXICAL ANALYSIS OUTPUT:")
pprint.pprint(tokens)
print("\n")

print("SYNTAX ANALYSIS OUTPUT:")
parser = Parser(tokens)
syntaxAnalysis = parser.parser()