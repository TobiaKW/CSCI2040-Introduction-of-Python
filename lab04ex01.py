class Stack():
    def __init__(self):
        self.storage = []

    def push(self, newValue):
        self.storage.append(newValue)

    def top(self):
        return self.storage[len(self.storage) - 1]

    def pop(self):
        result = self.top()
        self.storage.pop()
        return result

    def isEmpty(self):
        return len(self.storage) == 0


class CalcEngine():
    def __init__(self):
        self.dataStack = Stack()

    def pushOperand(self, value):
        self.dataStack.push(value)

    def currentOperand(self):
        return self.dataStack.top()

    def performBinaryOp(self, fun):
        right = self.dataStack.pop()
        left = self.dataStack.pop()
        self.dataStack.push(fun(left, right))

    def doAddition(self):
        self.performBinaryOp(lambda x, y: x + y)

    def doSubtraction(self):
        self.performBinaryOp(lambda x, y: x - y)

    def doMultiplication(self):
        self.performBinaryOp(lambda x, y: x * y)

    def doDivision(self):
        self.performBinaryOp(lambda x, y: x / y)
        
    def doModulo(self):
        # your code here
        self.performBinaryOp(lambda x, y: x % y)
    
    def doPower(self):
        # your code here
        self.performBinaryOp(lambda x, y: x ** y)

    def doTextOp(self, op):
        if (op == '+'):
            self.doAddition()
        elif (op == '-'):
            self.doSubtraction()
        elif (op == '*'):
            self.doMultiplication()
        elif (op == '/'):
            self.doDivision()
        elif (op == '%'):   # don't update CalcEngine here
            self.doModulo()
        elif (op == '^'):
            self.doPower()
        
class CalcEngineNew(CalcEngine):
    def __init__(self):
        super().__init__()        
        
    def doDivision(self):
        # your code here
        if self.dataStack.top() == 0:
             print("divide by 0!")
             exit(1)
        else:
            super().doDivision()
        
    def doModulo(self):
        # your code here
        if self.dataStack.top() == 0:
            print("modulo by 0!")
            exit(1)
        else:
            super().doModulo()
    
class RPNCalculator():
    operators = ['+', '-', '*', '/', '%', '^']

    def __init__(self):
        # your code here
        self.engine = CalcEngineNew()

    def eval(self, line):
        # your code here
        tokens = line.split()
        for token in tokens:
            if token in self.operators:
                self.engine.doTextOp(token)
            else:
                self.engine.pushOperand(int(token))
        return self.engine.currentOperand()


    def run(self):
        while True:
            line = input("type an expression: ")
            if len(line) == 0:
                break
            print(self.eval(line))

if __name__ == '__main__':
    cal = RPNCalculator()
    cal.run()
