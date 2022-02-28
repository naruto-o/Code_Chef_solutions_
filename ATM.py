# https://www.codechef.com/LP0TO101/submit/HS08TEST
# code for the above challenge
# solution 1
def main():
    withdrawl,balance = tuple(raw_input().split())
    withdrawl = int(withdrawl)
    balance = float(balance)
    if withdrawl % 5 == 0 and balance > (withdrawl+0.5):
        print balance - (withdrawl + 0.5)
    else:
        print balance

if __name__ == '__main__':
    main()

#     solution 2 for this problem 
    
    try:
    x,y = map(float, input().split())
    if x <= y-0.5 and x % 5==0:
        print("%.2f"%(y-x-0.50))
    else:
        print("%.2f"%y)
    
except:
    pass
 

   
