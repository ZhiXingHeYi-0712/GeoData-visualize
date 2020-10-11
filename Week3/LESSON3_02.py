init = [1 for i in range(20)]
grid = 20

for i, e in enumerate(init):
    if i+1 <= grid:
        print("放下了第{}个石子".format(i+1))
    else:
        print('走到尽头了')
        exit(0)
print('石子放完了')