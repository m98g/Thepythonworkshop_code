import re

customers = ["Xander Harris", "Jennifer Smith", "Timothy Jones", "Amy Alexandrescu",
 "Peter Price", "Weifung Xu"]

winners = []

pattern = "[Xx]"

for x in customers:
    result = re.search(pattern, x)
    if result == None:
        pass
    else:
        winners.append(x)

print(winners)

