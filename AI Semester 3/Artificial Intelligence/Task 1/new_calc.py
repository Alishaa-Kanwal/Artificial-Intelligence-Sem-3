class Calculator:
    def __init__(self):
        self.operators={
            '^':(3,lambda x,y: x ** y),
            '*':(2,lambda x,y: x * y),
            '/':(2,lambda x,y: x / y),
            '%': (2,lambda x,y: x % y),
            '+': (1,lambda x,y: x + y),
            '-': (1,lambda x,y: x - y),
        }
    def parse_exp(self,exp):
        tokens=[]
        curr_num= ""
        i= 0
        while i< len(exp):
            char= exp[i]            
            if char.isdigit() or (char== '.' and curr_num):
                curr_num +=char
            else:
                if curr_num:
                    tokens.append(curr_num)
                    curr_num= ""
                
                if char in '+-*/%^()':
                    tokens.append(char)

                if char== '(' and i > 0 and exp[i - 1].isdigit():
                    tokens.append('*')
            i = i+1
        
        if curr_num:
            tokens.append(curr_num)
        return tokens

    def evaluate(self, exp):
        tokens= self.parse_exp(expression)
        try:
            result= self._evaluate_exp(tokens)
            print(f"Final Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

    def _evaluate_exp(self,tokens):
        def apply_opr(opr,values):
            if len(values)< 2:
                raise ValueError("Insufficient values in the stack.")
            opr= opr.pop()
            right= values.pop()
            left= values.pop()
            opr_result= self.opr[opr][1](float(left),float(right))
            print(f"Step: {left} {opr} {right} = {opr_result}")
            values.append(opr_result)

        def precedence(op):
            return self.operators[op][0] if op in self.operators else 0
        values= []
        opr= []
        i= 0

        while i < len(tokens):
            token = tokens[i]

            if token.replace('.','',1).isdigit():
                values.append(float(token))
            elif token =='(':
                opr.append(token)
            elif token ==')':
                while opr and opr[-1]!='(':
                    apply_opr(opr,values)
                opr.pop()
                print(f"Bracket Solved: Current value = {values[-1]}")
            elif token in self.operators:
                while (opr and opr[-1] in self.operators and
                       precedence(opr[-1])>=precedence(token)):
                    apply_opr(opr,values)
                opr.append(token)
            i =i+1
        while opr:
            if len(values)< 2:
                raise ValueError("Insufficient values.")
            apply_opr(opr, values)
        if len(values)!= 1:
            raise ValueError("No fully evaluated Expression")
        return values[0]
if __name__=="__main__":
    calc =Calculator()
    expression= input("Enter an arithmetic expression: ")
    calc.evaluate(expression)
