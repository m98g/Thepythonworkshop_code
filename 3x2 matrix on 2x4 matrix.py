X = [[1, 2],[4, 5],[3, 6]]
Y = [[1,2,3,4],[5,6,7,8]]

result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):

            result[i][j] += X[i][k] * Y[k][j]
            print(result)


for r in result:
    print(r)