import unittest

class Solution:
    def operate(self, op, num1, num2):
        num1, num2 = int(num1), int(num2)
        if op == "+":
            return num2 + num1
        if op == "-":
            return num2 - num1
        if op == "*":
            return num2 * num1
        if op == "/":
            return num2 / num1

    def evalRPN(self, tokens: 'List[str]') -> 'int':
        ops = ["+", "-", "*", "/"]
        stack = []

        while len(tokens) > 0:
            token = tokens.pop(0)

            if token in ops:
                stack.append(self.operate(token, stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        
        return int(stack[0])

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testEvalRPN1(self):
        tokens = ["2", "1", "+", "3", "*"]
        expected = 9
        actual = self.solution.evalRPN(tokens)
        self.assertEqual(actual, expected)

    def testEvalRPN2(self):
        tokens = ["4", "13", "5", "/", "+"]
        expected = 6
        actual = self.solution.evalRPN(tokens)
        self.assertEqual(actual, expected)

    def testEvalRPN3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        expected = 22
        actual = self.solution.evalRPN(tokens)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()