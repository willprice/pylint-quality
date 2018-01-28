from pylint_complexity.method_length_checker import MethodLengthChecker


def register(linter):
    linter.register_checker(MethodLengthChecker(linter))
