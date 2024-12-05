import numpy as np

with open("04.in", "r") as f:
    ls = f.readlines()

# with open("04.test", "r") as f:
#     ls = f.readlines()

fd = {'X': 'M', 'M': 'A', 'A': 'S'}
r = 0

arr = np.empty((len(ls), len(ls[0]) - 1), dtype='<U1')
for i, l in enumerate(ls):
    for j, c in enumerate(l[:-1]):
        arr[i][j] = c

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i][j] == 'X':
            # checks to the right
            k = 1
            cc = 'X'
            if not (i + k >= arr.shape[0]):
                while arr[i + k][j] == fd[cc]:
                    if arr[i + k][j] == 'S':
                        r += 1
                        break
                    if i + k >= arr.shape[0] - 1:
                        break
                    cc = fd[cc]
                    k += 1
            # checks up right
            k = 1
            l = 1
            cc = 'X'
            if not (i + k >= arr.shape[0] or j + l >= arr.shape[1]):
                while arr[i + k][j + l] == fd[cc]:
                    if arr[i + k][j + l] == 'S':
                        r += 1
                        break
                    cc = fd[cc]
                    if i + k >= arr.shape[0] - 1 or j + l >= arr.shape[1] - 1:
                        break
                    k += 1
                    l += 1
            # checks up
            k = 1
            cc = 'X'
            if not (j + k >= arr.shape[1]):
                while arr[i][j + k] == fd[cc]:
                    if arr[i][j + k] == 'S':
                        r += 1
                        break
                    if j + k >= arr.shape[1] - 1:
                        break
                    cc = fd[cc]
                    k += 1
            # checks up left
            k = 1
            l = 1
            cc = 'X'
            if not (i - k < 0 or j + l >= arr.shape[1]):
                while arr[i - k][j + l] == fd[cc]:
                    if arr[i - k][j + l] == 'S':
                        r += 1
                        break
                    cc = fd[cc]
                    if i - k < 1 or j + l >= arr.shape[1] - 1:
                        break
                    k += 1
                    l += 1
            # checks to the left
            k = 1
            cc = 'X'
            if not (i - k < 0):
                while arr[i - k][j] == fd[cc]:
                    if arr[i - k][j] == 'S':
                        r += 1
                        break
                    if i - k < 1:
                        break
                    cc = fd[cc]
                    k += 1
            # checks up down left
            k = 1
            l = 1
            cc = 'X'
            if not (i - k < 0 or j - l < 0):
                while arr[i - k][j - l] == fd[cc]:
                    if arr[i - k][j - l] == 'S':
                        r += 1
                        break
                    cc = fd[cc]
                    if i - k < 1 or j - l < 1:
                        break
                    k += 1
                    l += 1
            # checks down
            k = 1
            cc = 'X'
            if not (j - k < 0):
                while arr[i][j - k] == fd[cc]:
                    if arr[i][j - k] == 'S':
                        r += 1
                        break
                    cc = fd[cc]
                    if j - k < 1:
                        break
                    k += 1
            # checks up down right
            k = 1
            l = 1
            cc = 'X'
            if not (i + k >= arr.shape[0] or j - l < 0):
                while arr[i + k][j - l] == fd[cc]:
                    if arr[i + k][j - l] == 'S':
                        r += 1
                        break
                    cc = fd[cc]
                    if i + k >= arr.shape[0] - 1 or j - l < 1:
                        break
                    k += 1
                    l += 1
print(r)
