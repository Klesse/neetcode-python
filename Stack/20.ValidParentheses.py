# First approach - too many if statements

def isValid(s):
    result = []
    for item in s:
        if item ==  "(" :
            result.append("(")
        if item ==  ")":
            if len(result) > 0:
                if result[-1] == "(":
                    result.pop()
                else:
                    return False
            else:
                return False
        if item ==  "[" :
            result.append("[")
        if item ==  "]":
            if len(result) > 0:
                if result[-1] == "[":
                    result.pop()
                else:
                    return False
            else:
                return False
        if item ==  "{" :
            result.append("{")
        if item ==  "}":
            if len(result) > 0:
                if result[-1] == "{":
                    result.pop()
                else:
                    return False
            else:
                return False
    if len(result) == 0:
        return True
    return False

# Second approach - way better solution with few if statements

def isValid(s):
    closed = {"}":"{", ")":"(", "]":"["}

    stack = []

    for item in s:
        if item in closed:
            if stack and stack[-1] == closed[item]:
                stack.pop()
            else:
                return False
        else:
            stack.append(item)
    return True if not stack else False