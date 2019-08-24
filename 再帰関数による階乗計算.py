#n階乗を計算する再帰関数
def func(n):
    if n==1:
        return 1
    return n * func(n-1)
