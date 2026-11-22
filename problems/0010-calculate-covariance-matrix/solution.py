def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Your code here
    n = len(vectors[0])
    rows = len(vectors)
    cov_matrix = [[0 for j in range(rows)] for i in range(rows)]

    for i in range(rows):
        for j in range(rows):
            sum_i = 0
            sum_j = 0

            for k in range(n):
                sum_i += vectors[i][k]
                sum_j += vectors[j][k]
                
            mean_i = sum_i / n
            mean_j = sum_j / n

            cov_sum = 0
            for k in range(n):
                cov_sum += (vectors[i][k] - mean_i) * (vectors[j][k] - mean_j)
            cov_matrix[j][i] = cov_sum / (n - 1)

    return cov_matrix