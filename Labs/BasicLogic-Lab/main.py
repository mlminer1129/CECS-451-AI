#----------------------------------------------------------------------------------------
#   A simple inference logic implementation
#   The original codes (APIs) is taken from the text book repository 
#   http://aima.cs.berkeley.edu/
#   
#   Modified by:                  
#   (c) 2020 Arjang Fahim
#
#   
#   Date: 7/22/2020
#   email: fahim.arjang@csulb.edu
#   version: 1.0.0
#----------------------------------------------------------------------------------------

from logic import *


# your code comes here

kb = PropKB()
kb.tell(expr('A | C'))
kb.tell(expr('B | ~C'))
print(kb.ask_if_true(expr('A | B')))

akb = PropKB()
akb.tell(expr('A | B'))
akb.tell(expr('~C|A'))
print(akb.ask_if_true(expr('A & B')))

print('Part 4: ', tt_entails(expr('A|C' and ('B| ~C')), expr('A|B')))