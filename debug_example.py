# THis is the debugged version. In the bugged version the basekt was defined 
# before the fucntion and basekt was set equal to that inital default basekt.
# However changes persist across calls and created a bug. The constants should
# be defined within the function and basekt should be set to None and not 
# a mutable object as the changes will persist.

def create_picnic_basket(healthy, hungry, basket=None):
    if basket is None:
        basket = ["orange", "apple"]
    if healthy:
        basket.append("strawberry")
    else:
        basket.append("jam")

    if hungry:
        basket.append("sandwich")
    return basket

# Reproducer
print("First basket:", create_picnic_basket(True, False))
print("Second basket:", create_picnic_basket(False, True, ["tea"]))
print("Third basket:", create_picnic_basket(True, True))
