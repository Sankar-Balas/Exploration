# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 12:29:41 2018

@author: MA953840
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:10:21 2018

@author: AR251426
"""

import sys
import ast
import astroid
from pylint import checkers
from pylint import interfaces
from pylint.checkers import utils
#import astroid.nodes

class whileChecker(checkers.BaseChecker):
    __implements__ = interfaces.IAstroidChecker
    name = 'fun-checker'
    msgs = {
    'W2201': ("while loop must have a break statement",
                  'break-missing',
                  'Emitted when no break statement is found within the loop'
                  'loop'
                  ),
              'W2202': ("Nested Loop/Conditions does not have Break",
                  'break-missing-inside-nested',
                  'Emitted when no break statement is found within the loop'
                  'loop'),
        }

    @utils.check_messages('fun-checker')
    def visit_while(self, node):
        body = node.body
        i = 0
        A = True
        B = True
        for a in body:
            i += 1
            if isinstance(a, astroid.While):
                # TO look for nested while
                for b in body[i:]:
                    # to find break inside nested loops
                    if isinstance(b, astroid.Break):
                        B = True
                        break
                    else:
                        B = False
            elif isinstance(a, ast.For):
                # TO look for nested loop
                for b in body[i:]:
                    # to find break inside nested loops
                    if isinstance(b, astroid.Break):
                        B = True
                        break
                    else:
                        B = False
            elif isinstance(a, astroid.Break):
                # to find break in the outer loop
                A = True
                if B:
                    return
                else:
                    self.add_message("W2202", node=node)
            else:
                A = False
        if A:
            # to check for atleast one break inside the loop
            return
        else:
            self.add_message("W2201", node=node)


def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(whileChecker(linter))
