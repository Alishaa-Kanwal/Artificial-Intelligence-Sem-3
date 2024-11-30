class Calculator:
    def __init__(self):
        self.operators = {
            '**': (3, lambda x, y: x ** y),
            '*': (2, lambda x, y: x * y),
            '/': (2, lambda x, y: x / y),
            '%': (2, lambda x, y: x % y),
            '+': (1, lambda x, y: x + y),
            '-': (1, lambda x, y: x - y),
        }

    def parse_expression(self, expression):
        tokens = []
        current_num = ""
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isdigit() or (char == '.' and current_num):
                current_num += char
            else:
                if current_num:
                    tokens.append(current_num)
                    current_num = ""

                if char in '+-*/%()':
                    if char == '-' and (i == 0 or expression[i-1] in '()+-*/%'):
                        current_num = '-'
                    else:
                        tokens.append(char)
                elif char == '*' and i + 1 < len(expression) and expression[i + 1] == '*':
                    tokens.append('**')
                    i += 1
                elif char == '(' and (i > 0 and expression[i-1].isdigit()):
                    tokens.append('*')  # Handle implicit multiplication
                    tokens.append(char)
                else:
                    tokens.append(char)
            i += 1
        if current_num:
            tokens.append(current_num)
        return tokens

    def evaluate(self, expression):
        tokens = self.parse_expression(expression)
        print(f"Expression: {tokens}")
        try:
            result = self._evaluate_expression(tokens)
            print(f"Final Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

    def _evaluate_expression(self, tokens):
        def apply_operator(operators, values):
            if len(values) < 2:
                raise ValueError("Insufficient values in the stack to apply operator.")
            operator = operators.pop()
            right = values.pop()
            left = values.pop()
            operation_result = self.operators[operator][1](float(left), float(right))
            print(f"Step: {left} {operator} {right} = {operation_result}")
            values.append(operation_result)

        def precedence(op):
            return self.operators[op][0] if op in self.operators else 0

        values = []
        operators = []
        i = 0

        while i < len(tokens):
            token = tokens[i]

            if token.replace('.', '', 1).isdigit():
                values.append(float(token))
                print(f"Added number: {token}")
            elif token == '(':
                operators.append(token)
                print(f"Added operator: '('")
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()  # Remove '('
                print(f"Solved expression inside parentheses: {values[-1]}")
            elif token in self.operators:
                while (operators and operators[-1] in self.operators and
                       precedence(operators[-1]) >= precedence(token)):
                    apply_operator(operators, values)
                operators.append(token)
                print(f"Added operator: {token}")

            i += 1

        # Final application of remaining operators
        while operators:
            if len(values) < 2:
                raise ValueError("Insufficient values for the remaining operators.")
            apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("The expression could not be fully evaluated.")

        return values[0]

if __name__ == "__main__":
    calc = Calculator()
    while True:
        try:
            expression = input("Enter an arithmetic expression (or 'exit' to quit): ")
            if expression.lower() == 'exit':
                break
            calc.evaluate(expression)
        except Exception as e:
            print(f"An error occurred: {e}")
