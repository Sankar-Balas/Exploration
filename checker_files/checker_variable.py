# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 11:04:18 2018

@author: MA953840
"""
import astroid
from pylint.interfaces import IAstroidChecker
from pylint.checkers import BaseChecker


class VariableChecker(BaseChecker):
    __implements__ = IAstroidChecker
    name = 'name-format'
    msgs = {'R2120': ("integer variable should start with 'i'",
                      'integer-name-format',
                      'Emitted when a bare return statement is found at the end of '
                      'function or method definition'),
              'R2121': ("string variable should start with 'st'",
                      'string-name-format',
                      'Emitted when a bare return statement is found at the end of '
                      'function or method definition'),
              'R2122': ("list variable should start with 'li'",
                      'list-name-format',
                      'Emitted when a bare return statement is found at the end of '
                      'function or method definition'),
              'R2123': ("tuple variable should start with 'tu'",
                      'tuple-name-format',
                      'Emitted when a bare return statement is found at the end of '
                      'function or method definition'),
              'R2124': ("dict variable should start with 'di'",
                      'dict-name-format',
                      'Emitted when a bare return statement is found at the end of '
                      'function or method definition'),
              'R2125': ("float variable should start with 'fl'",
                      'float-name-format',
                      'Emitted when a bare return statement is found at the end of '
                      'function or method definition'),
              'R2126': ("boolean variable should start with 'b'",
                      'boolean-name-format',
                      'Emitted when a bare return statement is found at the end of '
                      'function or method definition'),
    }

    options = (
        (
            'ignore-variables',
            {
                'default': False, 'type': 'yn', 'metavar': '<y_or_n>',
                'help': 'Allow returning non-unique integers',
            }
        ),

    )

    # @utils.check_messages('name-format')
    def visit_assign(self, node):

        var = list(node.get_children())[0].name
        # get variable name and check its naming type matches with format of datatype
        try:
            if list(node.get_children())[1].name == "int":
                if var.startswith("i"):
                    pass
                else:
                    self.add_message('integer-name-format', node=node)
            elif list(node.get_children())[1].name == "bool":
                if var.startswith("b"):
                    pass
                else:
                    self.add_message('boolean-name-format', node=node)
            elif list(node.get_children())[1].name == "str":
                if var.startswith("st"):
                    pass
                else:
                    self.add_message('string-name-format', node=node)
            elif list(node.get_children())[1].name == "list":
                if var.startswith("li"):
                    pass
                else:
                    self.add_message('list-name-format', node=node)
            elif list(node.get_children())[1].name == "tuple":
                if var.startswith("tu"):
                    pass
                else:
                    self.add_message('tuple-name-format', node=node)
            elif list(node.get_children())[1].name == "float":
                if var.startswith("fl"):
                    pass
                else:
                    self.add_message('float-name-format', node=node)
            elif list(node.get_children())[1].name == "dict":
                if var.startswith("di"):
                    pass
                else:
                    self.add_message('dict-name-format', node=node)
        except AttributeError:
            return


def register(linter):
    linter.register_checker(VariableChecker(linter))
