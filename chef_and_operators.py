
T = int(input())
while T > 0:
    m, n = map(int, input().split())
    if m > n:
        print(">")
    elif m < n:
        print("<")
    else:
        print("=")
    T = T - 1       
