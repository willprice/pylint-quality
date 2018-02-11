from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class MethodCountChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'method-count'
    priority = -1
    msgs = {
        'R1802': (
            'Too many methods in class', 'too-many-methods', 'Class has more than 10 methods in it'
        )
    }

    def __init__(self, linter=None):
        super(MethodCountChecker, self).__init__(linter)

    def visit_classdef(self, node):
        if len(list(node.mymethods())) > 10:
            self.add_message(self.msgs['R1802'][1], node=node)
