for _ in range(int(input())):
  n = int(input())
  rem = 0
  while n > 0:
    rem  = rem * 10 + rem %10
    n = n // 10
    print(rem)
