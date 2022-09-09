import collections

_defaults = {
    "apetisers": "Humus",
    "main": "Pizza",
    "desert": "Chocolate cake",
    "drink": "Water"
}
def prepare_menu(customizations):
    return collections.ChainMap(customizations, _defaults)
def print_menu(menu):
    for key, value in menu.items():
        print(f"As {key}: {value}")

menu1 = prepare_menu({})
menu3 = prepare_menu({"side": "French Fries"})
_defaults["main"] = "Pasta"
menu2 = prepare_menu({"drink": "Red Wine"})
print_menu(menu1)
print_menu(menu2)
print_menu(menu3)
