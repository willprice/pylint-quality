from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class ComplexityChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'function-complexity'
    priority = -1
    msgs = {}

    def __init__(self, linter=None):
        super(ComplexityChecker, self).__init__(linter)

    def visit_functiondef(self, node):
        pass
