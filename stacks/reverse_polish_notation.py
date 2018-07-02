"""Evaluate Reverse Polish Notation."""

# Evaluate the value of an arithmetic expression
# in Reverse Polish Notation.

# Valid operators are +, -, *, /.
# Each operand may be an integer or another expression.

# Note:
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid.
# That means the expression would always evaluate to a result
# and there won't be any divide by zero operation.

# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

from stacks.lib.stacks import ArrayStack


def postfix_evaluation(items):
    """Evaluate Reverse Polish Notation."""
    stack = ArrayStack()

    op = ["+", "-", "*", "/"]

    for item in items:
        if item not in op:
            stack.push(int(item))
        else:
            op2 = stack.top
            stack.pop()

            op1 = stack.top
            stack.pop()

            if item == "+":
                ans = int(op1 + op2)
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


def test_postfix_evaluation_one():
    """Test to check postfix_evaluation."""
    items = ["2", "1", "+", "3", "*"]
    assert (postfix_evaluation(items) == 9)


def test_postfix_evaluation_two():
    """Test to check postfix_evaluation."""
    items = ["4", "13", "5", "/", "+"]
    assert (postfix_evaluation(items) == 6)


def test_postfix_evaluation_three():
    """Test to check postfix_evaluation."""
    items = [
        "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"
    ]
    assert (postfix_evaluation(items) == 22)


# Leetcode Solution:
class Solution(object):
    """Solution for Leetcode."""

    def evalrpn(self, tokens):
        """Evaluate RPN.

        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        op = ["+", "-", "*", "/"]

        for item in tokens:
            if item not in op:
                stack.append(int(item))
            else:
                op2 = stack[-1]
                stack.pop()

                op1 = stack[-1]
                stack.pop()

                if item == "+":
                    ans = int(op1 + op2)
                    stack.append(ans)
                elif item == "-":
                    ans = int(op1 - op2)
                    stack.append(ans)
                elif item == "*":
                    ans = int(op1 * op2)
                    stack.append(ans)
                elif item == "/":
                    ans = int(float(op1) / float(op2))
                    stack.append(ans)
                else:
                    raise IOError(
                        "Invalid operator specified - {0}".format(item))

        return stack[-1]
