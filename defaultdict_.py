import collections
# the default action or function is called when there is not a key in the dict.
# that means when its defaultdict(list) the key is taken and an empty list 
# is created as the value if the function which is called can not find the area.

# The lambda function returns a list with an element in it

_audit = collections.defaultdict(lambda: ["Area created"])
def add_audit(area, action):
    #if the area is not allready in the dict the function defined in the brackets
    #of the default dict is called and the key value pair is created
    #using the callabe in the brackets after defaultdict.
    _audit[area].append(action)
    print(_audit)

def report_audit():
    for area, actions in _audit.items():
        print(f"{area} audit:")
        for action in actions:
            print(f"-{action}")
    print()

add_audit("HR", "Hired Sam")
add_audit("Finance", "Used 1000£")
add_audit("HR", "Hired Tom")


report_audit()