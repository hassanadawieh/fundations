

# "{}[]()"
# "{[()]}"
# "}[]()"


# Last IN First Out (LIFO)
# Stack
def is_valid_parenthesis(input_str):
    array = []
    mapping = {"(":")" , "{" : "}" , "[" : "]"}

    if input_str[0] in mapping.values():
         return False
    # elif input_str[len(input_str)-1] in mapping.keys():
    #      return False
    for char in input_str:
        if char in mapping.keys():
             array.append(char)
        elif char in mapping.values():
             if mapping[array[-1]] == char:
                  array.pop()
             else:
                  return False      
    if array:
         return False
    else:
         return True   

print(is_valid_parenthesis("({[]}[])[]"))      
