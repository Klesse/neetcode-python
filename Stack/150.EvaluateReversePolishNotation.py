# First and best approach

def evalRPN(tokens):
    stack = []

    operators = ["+","-","*","/"]

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            number1 = stack.pop()
            number2 = stack.pop()
            if token == "+":
                stack.append(number1+number2)
            elif token == "-":
                stack.append(number2-number1)
            elif token == "*":
                stack.append(number1*number2)
            elif token == "/":
                stack.append(int(number2/number1))
    return stack[0]