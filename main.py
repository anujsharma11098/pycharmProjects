def fibonaci(m,n):
    n1, n2 = 0, 1
    series=[]
    c=1
    while n2 <= n:
        if n2 > m:
            c+=1
        series.append(n2)
        n1, n2 = n2, n1 + n2
    print(c)
    print(series)


fibonaci(2,13)