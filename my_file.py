import numpy as np
import pandas as pd

matrix_A = np.random.randn(2,5)

matrix_B = np.random.randn(5,6)

final_result = np.matmul(matrix_A, matrix_B)

print(final_result.shape)