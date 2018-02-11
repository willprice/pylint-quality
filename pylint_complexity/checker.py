from pylint_complexity import MethodCountChecker, MethodLengthChecker


def register(linter):
    linter.register_checker(MethodLengthChecker(linter))
    linter.register_checker(MethodCountChecker(linter))
