# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 10:49:30 2018

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

class HeaderChecker(checkers.BaseChecker):
    __implements__ = interfaces.IAstroidChecker
    name = 'header-checker'
    msgs = {
    'R2118': ("code must have a script header",
                  'script-header-missing',
                  'Emitted when no script header is found'
                  'script header'
                  ),
    'R2117':("line number: %s must follow script header rules",
                  'script-header-format-missing',
                  'Emitted when no script header is not in format'
                  'script header structure'
                  ),
    'R2116':("end of header must have a blank line",
                  'script-header-blank-line-not-found',
                  'Emitted when no blank line at the end of script header'
                  'script header blan line'
                  ),
        }

    def visit_module(self, node):
        lineno = node.fromlineno + 1
        line = linecache.getline(node.root().file, lineno).lstrip()
        l1 = re.compile(r"^[#][---]")
        l2 = re.compile(r"^[#].[Module]")
        l3 = re.compile(r"^[#].[Objective]")
        l4 = re.compile(r"^[#].[TS]")
        l5 = re.compile(r"^[#].[TC]")
        l6 = re.compile(r"^[#].[Squish]")
        l7 = re.compile(r"^[#].[QT]")
        l8 = re.compile(r"^[#].[Python version]")
        l9 = re.compile(r"^[#].[Author]")
        l10 = re.compile(r"^[#].[Date of creation]")
        l11 = re.compile(r"^[#][---]")
        l12 = re.compile(r"^[#].[Modification HISTORY]")
        lx = re.compile(r"^[#\s\s]")
        ly = re.compile(r"^[#\s][^-]")
        if l1.match(line):
            pass
        else:
            # if headear is not found
            self.add_message("R2118", node=node)
            return
        i = 1
        lineno = i
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
                pass
            elif i == 9 and l9.match(line):
                pass
            elif i == 10 and l10.match(line):
                pass
            elif i == 11 and l11.match(line):
                break
            elif lx.match(line):
                # to find and accept empty or extension of previous statement
                i -= 1
            else:
                # when particular line mis-match the format
                self.add_message("R2117", args=(i,), node=node)
                break
            i += 1
        line = linecache.getline(node.root().file, lineno).lstrip()

        if l12.match(line):
            # Modification history may be appended anytime(not of fixed length)
            # looks for end of Header after completion of history
            while True:
                lineno += 1
                line = linecache.getline(node.root().file, lineno).lstrip()
                if ly.match(line):
                    pass
                elif l11.match(line):
                    break
                else:
                    break

        if len(line) == 0:
            # check for blank line after header
            return
        else:
            self.add_message("R2116", node=node)
            return

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(HeaderChecker(linter))

