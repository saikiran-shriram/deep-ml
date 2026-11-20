def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if mode == 'row' :
        for i in range(len(matrix)) :
            means.append(sum(matrix[i])/len(matrix[0]))
    if mode == 'column' :
        dict = {}
        for i in range(len(matrix[0])) :
            dict[i] = 0
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                dict[j] += matrix[i][j]
        for j in range(len(matrix[0])) :  
            means.append(dict[j]/len(matrix))
    return means