import astroid
import pylint.testutils

import pylint_complexity


class TestMethodCountChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = pylint_complexity.MethodCountChecker

    def test_11_methods_is_too_many(self):
        class_node = astroid.extract_node("""
        class TooManyMethods: #@
            def m1(self):
                pass

            def m2(self):
                pass

            def m3(self):
                pass

            def m4(self):
                pass

            def m5(self):
                pass

            def m6(self):
                pass

            def m7(self):
                pass

            def m8(self):
                pass

            def m9(self):
                pass

            def m10(self):
                pass

            def m11(self):
                pass
        """)
        with self.assertAddsMessages(
            pylint.testutils.Message(
                    msg_id='too-many-methods',
                    node=class_node
            )
        ):
            self.checker.visit_classdef(class_node)

    def test_10_methods_is_acceptable(self):
        class_node = astroid.extract_node("""
        class AcceptableNumberOfMethods: #@
            def m1(self):
                pass

            def m2(self):
                pass

            def m3(self):
                pass

            def m4(self):
                pass

            def m5(self):
                pass

            def m6(self):
                pass

            def m7(self):
                pass

            def m8(self):
                pass

            def m9(self):
                pass

            def m10(self):
                pass

        """)
        with self.assertNoMessages():
            self.checker.visit_classdef(class_node)
