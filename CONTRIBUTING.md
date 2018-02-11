# Adding a new checker

1. Create examples for checker to run on in `tests/system/examples`
2. Create unit test for checker `tests/test_<checker_name>.py`
   ```python
    import astroid
    import pylint.testutils

    from pylint_complexity import <checker_name>


    class TestMethodLengthChecker(pylint.testutils.CheckerTestCase):
        CHECKER_CLASS = <checker_name>.<CheckerClassName>
    ```
3. Create checker
   ```python
    from pylint.checkers import BaseChecker
    from pylint.interfaces import IAstroidChecker


    class <ClassName>(BaseChecker):
        __implements__ = IAstroidChecker

        name = '<checker_name>'
        priority = -1
        msgs = {
            'R18<rule-id>': (
                '<warning_message>', '<error_id>', '<detailed_description>'
            )
        }

        def __init__(self, linter=None):
            super(<ClassName>, self).__init__(linter)

   ```
4. Register the checker in the root `pylint_complexity.checker` file
   ```python
    from pylint_complexity import <CheckerClassName>


    def register(linter):
        linter.register_checker(<CheckerClassName>(linter))
   ```
5. Enable the checker's messages in `pylintrc` in the `enable` key. e.g.
   for a checker that asserts a message `my-message` the line
   `enable=...,my-message` should be present in `pylintrc`
