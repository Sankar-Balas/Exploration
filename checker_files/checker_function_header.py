# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:51:40 2018

@author: MA953840
"""


import sys
import ast
import re
import linecache
from pylint import checkers
from pylint import interfaces
from pylint.checkers import utils
#import astroid.nodes

class FunHeaderChecker(checkers.BaseChecker):
    __implements__ = interfaces.IAstroidChecker
    name = 'fun-header-checker'
    msgs = {
    'R2110': ("function must have a function header",
                  'function-header-missing',
                  'Emitted when no function header is found'
                  'function header'
                  ),
    'R2111':("line number: %s must follow function header rules",
                  'function-header-format-missing',
                  'Emitted when no function header is not in format'
                  'function header structure'
                  ),
    'R2112':("end of header must have a blank line",
                  'function-header-blank-line-not-found',
                  'Emitted when no blank line at the end of function header'
                  'function header blan line'
                  ),
        }

    def visit_functiondef(self, node):
        lineno = node.fromlineno - 1
        line = linecache.getline(node.root().file, lineno).lstrip()
        fhead = re.compile(r"#")
        l1 = re.compile(r"^[#][---]")
        l2 = re.compile(r"^[#]\s[Function]")
        l3 = re.compile(r"^[#]\s[Description]")
        l4 = re.compile(r"^[#]\s[Parameters]")
        l5 = re.compile(r"^[#]\s[return]")
        l6 = re.compile(r"^[#]\s[Programmer]")
        l7 = re.compile(r"^[#]\s[Created Date]")
        l8 = re.compile(r"^[#]\s[Modification HISTORY]")
        lx = re.compile(r"^[#\s\s]")
        ly = re.compile(r"^[#\s][^-]")
        while True:
            # to find the start of header
            lineno -= 1
            line = linecache.getline(node.root().file, lineno).lstrip()
            if fhead.match(line):
                pass
            else:
                break
        lineno += 1
        line = linecache.getline(node.root().file, lineno).lstrip()
        if l1.match(line):
            pass
        else:
            self.add_message("R2110", node=node)
            return
        i = 1
        while True:
            # To match the format with specified format
            line = linecache.getline(node.root().file, lineno).lstrip()
            lineno += 1
            if i == 1 and l1.match(line):
                pass
            elif i == 2 and l2.match(line):
                pass
            elif i == 3 and l3.match(line):
                pass
            elif i == 4 and l4.match(line):
                pass
            elif i == 5 and l5.match(line):
                pass
            elif i == 6 and l6.match(line):
                pass
            elif i == 7 and l7.match(line):
                pass
            elif i == 8 and l8.match(line):
                break
            elif lx.match(line):
                # to find and accept empty or extension of previous statement
                i -= 1
            else:
                # when particular line mis-match the format
                self.add_message("R2111", args=(i,), node=node)
                break
            i += 1
        if l8.match(line):
            # Modification history may be appended anytime(not of fixed length)
            # looks for end of Header after completion of history
            while True:
                line = linecache.getline(node.root().file, lineno).lstrip()
                lineno += 1
                if ly.match(line):
                    pass
                elif l1.match(line):
                    break
                else:
                    break
        line = linecache.getline(node.root().file, lineno).lstrip()
        if len(line) == 0:
            # check for blank line after header
            return
        else:
            self.add_message("R2112", node=node)
            return

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(FunHeaderChecker(linter))
