import itertools

players = ["White", "Black"]

turns = itertools.cycle(players)

countdown = itertools.count(10, -1)

print([turn for turn in itertools.takewhile(lambda x: next(countdown) > 0, turns)])


###his is the "round-robin" algorithm for allocating actions (in this case, making a chess 
###move) to resources (in this case, the players), and has many more applications than 
###board games. A simple way to do load balancing between multiple servers in a web 
###service or database application is to build an infinite sequence of the available servers 
###and choose one in turn for each incoming request.