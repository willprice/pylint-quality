import astroid
import pylint.testutils

from pylint_complexity import method_length_checker


class TestMethodLengthChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = method_length_checker.MethodLengthChecker

    def test_function_with_more_than_10_statements_is_too_long(self):
        self.assertTooLong("""
            def longFunction(): #@
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

    def test_function_with_10_statements_is_acceptable(self):
        self.assertNotTooLong("""
        def acceptableLengthFunction(self): #@
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
        """)

    def test_function_length_doesnt_count_comments(self):
        self.assertNotTooLong("""
        def acceptableLengthFunctionWithComments(self): #@
            x = 1
            x = 2
            x = 3
            x = 4
            x = 5
            x = 6
            x = 7
            x = 8
            x = 9
            # comments aren't included in the method LOC
            x = 10
        """)

    def test_blank_lines_in_function_dont_count_as_statements(self):
        self.assertNotTooLong("""
            def longFunction(): #@










                x = 11
        """)

    def test_multiline_statements_count_as_one_line_of_code(self):
        self.assertNotTooLong("""
        def acceptableFunctionWithSplitExpression(self):
            x = 1
            x = 2
            x = 3
            x = 4
            x = 5
            x = 6
            x = 7
            x = 8
            x = 9
            x = 10 + \
                11
        """)

    def test_method_with_11_statements_is_too_long(self):
        self.assertTooLong("""
        class SomeClass():
            def overlyLongMethod(self): #@
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

    def test_method_with_10_statements_isnt_too_long(self):
        self.assertNotTooLong("""
        class SomeClass():
            def overlyLongMethod(self): #@
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
        """)

    def assertNotTooLong(self, function: str):
        func_node = astroid.extract_node(function)
        with self.assertNoMessages():
            self.checker.visit_functiondef(func_node)

    def assertTooLong(self, function: str):
        func_node = astroid.extract_node(function)
        with self.assertAddsMessages(
                pylint.testutils.Message(
                        msg_id='method-too-long',
                        node=func_node
                )
        ):
            self.checker.visit_functiondef(func_node)


