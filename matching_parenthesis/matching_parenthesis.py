def isBalanced(param):
    parenthesis_found = []
    for s in param:
        if _isOpened(s):
            parenthesis_found.append(s)

        elif _isClosed(s):
            if len(parenthesis_found) == 0:
                return False

            last = parenthesis_found[-1]
            parenthesis_found.pop()
            if not _doMatch(last, s):
                return False
    return True if len(parenthesis_found) == 0 else False




def recIsBalanced(param, stack=""):
    if param == "":
        return True if stack == "" else False

    if _isOpened(param[0]):
        return recIsBalanced(param[1:], stack + param[0])

    if _isClosed(param[0]):
        if len(stack) == 0:
            return False

        if _doMatch(stack[-1], param[0]):
            return recIsBalanced(param[1:], stack[:-1])




def _isOpened(c):
    return True if c in ["(","[","{"] else False

def _isClosed(c):
    return True if c in [")","]","}"] else False

def _doMatch(openC, closeC):
    if     ( closeC == ")" and openC == "(" ) \
        or ( closeC == "}" and openC == "{" ) \
        or ( closeC == "]" and openC == "[" ):
        return True
    return False
