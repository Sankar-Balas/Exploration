# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:11:19 2018

@author: MA953840
"""


import sys
import ast
import astroid
import linecache
from pylint.interfaces import IAstroidChecker, HIGH
from pylint.checkers.utils import check_messages
from pylint import checkers
from pylint import interfaces
from pylint.checkers import utils
#import astroid.nodes

class CommentsChecker(checkers.BaseChecker):
    __implements__ = interfaces.IAstroidChecker
    name = 'comments-checker'
    msgs = {
    'C0198': ('Bad docstring quotes in %s, expected """, given %s',
              'bad-docstring-quotes',
              'Used when a docstring does not have triple double quotes.'),
    'C0199': ('First line empty in %s docstring',
              'docstring-first-line-empty',
              'Used when a blank line is found at the beginning of a docstring.'),
    'C0197': ('Missing docstring in %s',
              'docstring-not-found',
              'Used no docstring is used'),
                  }

    def visit_while(self, node):
        self._check_docstring('while', node)

    def visit_for(self, node):
        self._check_docstring('for', node)

    def visit_if(self, node):
        self._check_docstring('if', node)

    def _check_docstring(self, node_type, node):
        # check doctring for loops/conditions which calls this function
        lineno = node.lineno + 1
        line = linecache.getline(node.root().file, lineno).lstrip()
        if line:
            if line.find('"""') == 0:
                # correct docstring format
                return
            if line and '\'\'\'' in line:
                quotes = '\'\'\''
            elif line and line[0] == '"':
                quotes = '"'
            elif line and line[0] == '\'':
                quotes = '\''
            else:
                quotes = False
                self.add_message("C0197", node=node,
                                 args=(node_type,), confidence=HIGH)
            if quotes:
                # bad docstring
                self.add_message('bad-docstring-quotes', node=node,
                                 args=(node_type, quotes), confidence=HIGH)
        else:
            # doctring not found
            self.add_message("C0199", node=node, args=(node_type,),
                             confidence=HIGH)


def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(CommentsChecker(linter))
