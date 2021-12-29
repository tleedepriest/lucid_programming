"""
Use a stack to determine whether or not a set of parathesis
is balanced or not.

(), ()(), (({[]})) --> Balanced
((), {{{)]), ()()}}, )) --> Not Balanced
last example of not balanced edge case bc
doesn't include
"""
from stack import Stack

def is_match(p1, p2):
    print(p1)
    print(p2)
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    
    return False


def is_paren_balanced(paren_string):
    """
    paren string containing only openining and closing
    parents
    """
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[":
            s.push(paren)
        else: #closing parenthesis
            if s.is_empty():
                is_balanced = False
            else: # pushed opening in stack
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index+=1

    if s.is_empty() and is_balanced:
        return True
    return False

if  __name__ == "__main__":
    parens = "[[[]]]"
    print(is_paren_balanced(parens))
    parens = "{{{{]"
    print(is_paren_balanced(parens))
