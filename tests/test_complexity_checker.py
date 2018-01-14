import astroid
import pylint.testutils

import complexity_checker


class TestComplexityChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = complexity_checker.ComplexityChecker

    def test_function_with_more_than_10_statements_is_too_long(self):
        func_node = astroid.extract_node("""
            def longMethod(): #@
                x = 1
                x = 2
                x = 3
                x = 4
                x = 5
                x = 6
                x = 7
                x = 8
                x = 9
                x = 10
                x = 11
        """)
        with self.assertAddsMessages(
                pylint.testutils.Message(
                        msg_id='function-too-complex',
                        node=func_node
                )
        ):
            self.checker.visit_functiondef(func_node)
