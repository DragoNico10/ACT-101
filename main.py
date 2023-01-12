import msvcrt
import random
import time


def roll():
    print('Rolling...')
    time.sleep(random.random()*2)
    n=random.randint(1,6)
    if(n==1):
        print("[-----]") 
        print("[     ]") 
        print("[  ♦  ]") 
        print("[     ]") 
        print("[-----]")
    elif(n==2):
        print("[-----]") 
        print("[     ]") 
        print("[♦   ♦]") 
        print("[     ]") 
        print("[-----]")
    elif(n==3):
        print("[-----]") 
        print("[    ♦]") 
        print("[  ♦  ]") 
        print("[♦    ]") 
        print("[-----]")
    elif(n==4):
        print("[-----]") 
        print("[♦   ♦]") 
        print("[     ]") 
        print("[♦   ♦]") 
        print("[-----]")
    elif(n==5):
        print("[-----]") 
        print("[♦   ♦]") 
        print("[  ♦  ]") 
        print("[♦   ♦]") 
        print("[-----]")
    elif(n==6):
        print("[-----]") 
        print("[♦   ♦]") 
        print("[♦   ♦]") 
        print("[♦   ♦]") 
        print("[-----]")
    else:
        print("[-----]") 
        print("[     ]") 
        print("[  ?  ]") 
        print("[     ]") 
        print("[-----]")
    

    print('Roll again? (Y, N)')
    while True:
        response=msvcrt.getwch()
        if(response=='y'):
            roll()
            break
        elif(response=='n'):
            print('closing instance...')
            time.sleep(1.5)
            break
        else:
            print(f'Value {response} is not valid, try Y or N?')
        

roll()