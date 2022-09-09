import dataclasses

@dataclasses.dataclass
class Point:
    x: int
    y: int

p = Point(x=10, y=20)
p2 = Point(x=10, y=20)

print(p == p2)

print(dataclasses.asdict(p))