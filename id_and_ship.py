# https://www.codechef.com/LP0TO101/submit/FLOW010
# link for above challenge
T = int(input())
for i in range(T):
    toy_input = input().lower()
    if(toy_input == 'b'):
        print("BattleShip")
    elif(toy_input == 'c'):
        print("Cruiser")
    elif(toy_input=='d'):
        print("Destroyer")
    elif(toy_input=='f'):
        print('Frigate')
    
    
