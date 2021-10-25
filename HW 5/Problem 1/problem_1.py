### Problem 1

X = [[10,8],
    [2 ,4],
    [1 ,7]]

def transpose(matrix):
    results = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    # Iterate over columns of `matrix`
    for i in range(len(matrix[0])):
        # Iterate over rows of `matrix`
        for j in range(len(matrix)):
            results[i][j] += matrix[j][i]
    return(results)

transpose(X)