a = []
for i in range(1, 1000000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        a.append(i)
print(a)
