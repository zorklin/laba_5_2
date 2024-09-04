size = 7
array = [[j - i for j in range(size)] for i in range(size)]
for row in array:
    print(*row)
