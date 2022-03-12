# https://www.codechef.com/LP0TO101/problems/FLOW013
# link for above challeng
T = int(input())
for i in range(T):
    (a , b, c) = map(int , input().split())
    ans = a + b+ c 
    if(ans==180):
        print("YES")
    else:
        print("NO")
