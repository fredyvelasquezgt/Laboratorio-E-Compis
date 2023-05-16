#Fredy Velasquez
#201011

from Lexer import Lexer
from Parser import Parser
from Automata import Automata
parser = Parser._from_file('yapar.txt')
print(parser.grammar.productions)
parser.draw_automata()