"""
reverse string using stack data structure
"""
from stack import Stack


def reverse_string(string):
    reverse_string = ""
    s = Stack()
    for letter in string:
        s.push(letter)
    while not s.is_empty():
        rev = s.pop()
        reverse_string+=rev
    return reverse_string
        

if __name__ == "__main__":
    rev = reverse_string("hello there")
    print(rev)
