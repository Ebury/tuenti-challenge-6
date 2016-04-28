import math

with open('submitInput.txt', 'r') as f:
    inputs = f.readlines()

n_cases = inputs[0]
inputs = inputs[1:]


def tables(i: int):
    if i == 0:
        return 0
    elif i in (1, 2):
        return 1
    elif i > 0:
        return math.ceil((i-2)/2)

outputs = [tables(int(i)) for i in inputs]

with open('submitOutput.txt', 'w') as f:
    f.writelines(['Case #{}: {}\n'.format(i+1, value) for (i, value) in enumerate(outputs)])
