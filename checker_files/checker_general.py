# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:36:17 2018

@author: MA953840
"""


import sys
import ast
import linecache
import re
from pylint import checkers
from pylint import interfaces
from pylint.checkers import utils
#import astroid.nodes

class GeneralChecker(checkers.BaseChecker):
    __implements__ = interfaces.IAstroidChecker
    name = 'general-checker'
    msgs = {
    'W2110': ("Script should have Logger.startlog",
                  'startlog-missing',
                  'Emitted when no startlog is found'
                  'Logger.startlog call'
                  ),
    'W2111': ("Script should have Logger.stoplog",
                  'stoplog-missing',
                  'Emitted when no stoplog is found'
                  'Logger.stoplog call'
                  ),
    'W2112': ("AttachToApplication found in lineno: %s",
                  'attach-to-application-found',
                  'Emitted when AttachToApplication is found'
                  'AttachToApplication call'
                  ),
    'W2113': ("Hardcoded path found in lineno: %s",
                  'hardcoded-path-found',
                  'Emitted when hardcoded-path is found'
                  'Hardcoded paths'
                  ),
    'W2114': ("lineno: %s has snooze without comments",
                  'snooze-sleep-without-comments',
                  'Emitted when commenst for snooze and sleep is not found'
                  'snooze sleep usage'
                  ),
        }

    def visit_module(self, node):
        stoplog = re.compile(r"Logger.stopLog|Cleanup")
        startlog = re.compile(r"Logger.startLog|commonPrecondition|globalPreCondition|homeSettingsPreCondition")
        hardpath = re.compile(r'.*?[a-zA-Z]\:(\\\\|\\).*')
        snooze = re.compile(r"snooze")
        attachApp = re.compile(r"attachToApplication|launchApplication")

        startlog_f = False
        stoplog_f = False
        limit = node.block_range(0)[1]

        for i in range(1, limit + 1):
            # iterate line by line to find the specified executions/calls
            lineno = i
            cline = linecache.getline(node.root().file, lineno).lstrip()
            pline = linecache.getline(node.root().file, lineno-1).lstrip()
            if startlog.search(cline):
                if not cline.startswith("#"):
                    startlog_f = True
            if stoplog.search(cline):
                if not cline.startswith("#"):
                    stoplog_f = True
            if hardpath.search(cline):
                if not cline.startswith("#"):
                    self.add_message("W2113", args=(lineno,), node=node)
            if snooze.search(cline):
                if not cline.startswith("#"):
                    if not pline.startswith("#"):
                        self.add_message("W2114", args=(lineno,), node=node)
            if attachApp.search(cline):
                if not cline.startswith("#"):
                    self.add_message("W2112", args=(lineno,), node=node)
        if not startlog_f:
            self.add_message("W2110", node=node)
        if not stoplog_f:
            self.add_message("W2111", node=node)
        return

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(GeneralChecker(linter))
