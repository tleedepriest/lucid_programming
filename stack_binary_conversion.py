"""
Use Stack data structure to convert numbers to binary
value


Example 242
                           binary rep (from bottom to top)
                           ----------
242 / 2 = 121 -> remainder 0
121 / 2 = 60 -> remainder  1
60 / 2 = 30 -> remainder   0
30 / 2 = 15 - remainder    0
15 / 2 = 7 -> remainder    1
7 / 2 = 3 -> remainder     1
3 /2 - > 1 -> remainder    1
/ / 2 -> 0 -> remainder    1
"""
from stack import Stack

def convert_to_binary(number):
    s = Stack()
    while number > 0:
        remainder = number%2
        s.push(remainder)
        number = number // 2
    
    bin_rep = ""
    while not s.is_empty():
        bin_rep+=str(s.pop())
    return bin_rep

if __name__ == "__main__":
    rep = convert_to_binary(1232)
    print(rep)
    rep = convert_to_binary(242)
    print(rep)
