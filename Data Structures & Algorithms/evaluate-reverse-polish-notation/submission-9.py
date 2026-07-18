class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                b = total.pop()
                a = total.pop()
                if token == "+":
                    total.append(a + b)
                elif token == "-":
                    total.append(a - b)
                elif token == "*":
                    total.append(a * b)
                elif token == "/":
                    total.append(int(a / b))
            else:
                total.append(int(token))
        return total[0]
        