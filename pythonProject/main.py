import numpy as np
import json
x = json.loads(input())
res = np.sin(x)
for j in range(len(res)-1):
    for i in range(len(res)-1-j):
        if res[i] > res[i+1]:
            res[i], res[i + 1] = res[i + 1], res[i]
            x[i], x[i + 1] = x[i+1], x[i]
print(x)