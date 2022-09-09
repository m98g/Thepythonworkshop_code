# This is a comment

### pbd can also be activated in a cli with -> python3.X –m pdb script_name.py

this = "is the first line to execute"

def secret_sauce(number):
    # this acts as an activation point for the pbd debugging tool which 
    # after each execution will tell you what happend and wait for user input
    # very useful for debugging.
    breakpoint()
    if number <= 10:
        return number + 10
    else:
        return number - 10

def magic_operation(x, y):
    res = x + y
    res *= y
    res /= x
    res = secret_sauce(res)
    return res

print(magic_operation(2, 10))