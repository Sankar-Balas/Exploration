# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:10:21 2018

@author: AR251426
"""

import sys
import ast
from pylint import checkers
from pylint import interfaces
from pylint.checkers import utils
#import astroid.nodes

class FunChecker(checkers.BaseChecker):
    __implements__ = interfaces.IAstroidChecker
    name = 'function-name-format'
    msgs = {
    'R2119': ("functions should start with lowercase letter",
                  'function-name-format',
                  'Emitted when a bare return statement is found at the end of '
                  'function or method definition'
                  ),
        }

    @utils.check_messages('function-name-format')
    def visit_functiondef(self, node):
        "check the function name format"
        # check whether the function name starts with lower case
        if node.name != "Precondition":
            if node.name != node.name.capitalize():
                pass
            else:
                self.add_message('function-name-format', node=node)




def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(FunChecker(linter))

