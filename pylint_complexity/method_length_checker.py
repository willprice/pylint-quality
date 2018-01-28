import astroid
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class MethodLengthChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'method-complexity'
    priority = -1
    msgs = {
        'R1801': (
            'Method is too long', 'method-too-long', 'Method has more than 10 statements in it'
        )
    }

    def __init__(self, linter=None):
        super(MethodLengthChecker, self).__init__(linter)

    def visit_functiondef(self, node):
        statement_count = len([child for child in node.get_children()
                               if isinstance(child, astroid.node_classes.Statement)])

        if statement_count > 10:
            self.add_message(self.msgs['R1801'][1], node=node)
