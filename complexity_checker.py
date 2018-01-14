import astroid
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class ComplexityChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'function-complexity'
    priority = -1
    msgs = {
        'R1801': (
            'Function is too long', 'function-too-long', 'Function has more than 10 statements in it'
        )
    }

    def __init__(self, linter=None):
        super(ComplexityChecker, self).__init__(linter)

    def visit_functiondef(self, node):
        statement_count = len([child for child in node.get_children()
                               if isinstance(child, astroid.node_classes.Statement)])

        if statement_count > 10:
            self.add_message('function-too-complex', node=node)
