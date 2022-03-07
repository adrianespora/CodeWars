def valid_parentheses(string):
    open = '('
    close = ')'
    cuenta = 0
    for x in string:
        if cuenta >= 0:
            if x == open:
                cuenta = cuenta +1
            elif x == close:
                cuenta = cuenta -1
            else:
                continue
    if cuenta == 0:
        return True      
    else:
        return False
    

 
valid_parentheses('(())((()())())')  # =>  true
valid_parentheses("()") #              =>  true
#valid_parentheses(")(()))")     #   =>  false
#valid_parentheses("(")         #    =>  false
#valid_parentheses('hi(hi))()') #false
#valid_parentheses("hi(hi)()") #True
#valid_parentheses("hi())(") # False

"""
def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
    """