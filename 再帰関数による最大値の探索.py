#最大値を求めるアルゴリズム
def findMax(A, l, r):
    #Aの要素をl~m、m~rに2分割
    m = (l+r)//2
    #要素が残り1つの場合
    if l==r-1:
        return A[l]
    else:
        u = findMax(A,l,m)#前半部の最大値を求める
        v = findMax(A,m,r)#後半部の最大値を求める
        x = max(u,v)
    return x
