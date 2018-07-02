"""Evaluate Prefix Notation."""

# Evaluate the value of an arithmetic expression in Prefix Notation

# Valid operators are +, -, *, /.
# Each operand may be an integer or another expression.

# Note:
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid.
# That means the expression would always evaluate to a result
# and there won't be any divide by zero operation.

# Input: ["+", "9", "*", "2", "6"]
# Output: 21

# Input: ["-", "+", "8", "/", "6", "3", "2"]
# Output: 8

# Input: ["-", "+", "7", "*", "4", "5", "+", "2"]
# Output: 25

from stacks.lib.stacks import ArrayStack


def prefix_evaluation(items):
    """Evaluate Prefix Notation."""
    stack = ArrayStack()

    op = ["+", "-", "*", "/"]

    for item in reversed(items):
        if item not in op:
            stack.push(int(item))
        else:
            op1 = stack.top
            stack.pop()

            op2 = stack.top
            stack.pop()

            if item == "+":
                ans = int(op1 + op2)
                print "{0} + {1} = {2}".format(op1, op2, ans)
                stack.push(ans)
            elif item == "-":
                ans = int(op1 - op2)
                stack.push(ans)
            elif item == "*":
                ans = int(op1 * op2)
                stack.push(ans)
            elif item == "/":
                ans = int(float(op1) / float(op2))
                stack.push(ans)
            else:
                raise IOError("Invalid operator specified - {0}".format(item))

    return stack.top


def test_prefix_evaluation_one():
    """Test to check prefix_evaluation."""
    items = ["+", "9", "*", "2", "6"]
    assert(prefix_evaluation(items) == 21)


def test_postfix_evaluation_two():
    """Test to check prefix_evaluation."""
    items = ["-", "+", "8", "/", "6", "3", "2"]
    assert(prefix_evaluation(items) == 8)


def test_postfix_evaluation_three():
    """Test to check prefix_evaluation."""
    items = ["-", "*", "+", "4", "3", "2", "5"]
    assert(prefix_evaluation(items) == 9)
