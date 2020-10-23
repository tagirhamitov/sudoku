import pycosat
import math

n = 9
field = []
for i in range(n):
    s = input()
    row = [0 if c == '*' else int(c) for c in s]
    field.append(row)


def to_n(i, j, k):
    return i * n * n + j * n + k + 1


def from_n(x):
    return (x - 1) // (n * n), ((x - 1) % (n * n)) // n, ((x - 1) % n) + 1


clauses = []
for i in range(n):
    for j in range(n):
        cell = []
        for k in range(n):
            for k1 in range(n):
                if k1 != k:
                    clauses.append([-to_n(i, j, k), -to_n(i, j, k1)])
            for j1 in range(n):
                if j1 != j:
                    clauses.append([-to_n(i, j, k), -to_n(i, j1, k)])
                if j1 != i:
                    clauses.append([-to_n(i, j, k), -to_n(j1, j, k)])
            cell.append(to_n(i, j, k))
        clauses.append(cell)

N = int(math.sqrt(n))
for I in range(N):
    for J in range(N):
        for i1 in range(I * 3, (I + 1) * 3):
            for j1 in range(J * 3, (J + 1) * 3):
                for i2 in range(I * 3, (I + 1) * 3):
                    for j2 in range(J * 3, (J + 1) * 3):
                        if i1 == i2 and j1 == j1:
                            continue
                        for k in range(n):
                            clauses.append([-to_n(i1, j1, k), -to_n(i2, j2, k)])

for i in range(n):
    for j in range(n):
        if field[i][j] != 0:
            clauses.append([to_n(i, j, field[i][j] - 1)])

answer = pycosat.solve(clauses)
print()
if answer == 'UNSAT':
    print('UNSOLVABLE')
else:
    for x in answer:
        if x > 0:
            i, j, k = from_n(x)
            field[i][j] = k
    for i in range(n):
        for j in range(n):
            print(field[i][j], end='')
            if j == 2 or j == 5:
                print('|', end='')
        print()
        if i == 2 or i == 5:
            print('-' * 11)
