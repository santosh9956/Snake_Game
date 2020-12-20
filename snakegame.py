
import random

def gamewin(a,b):
    if b==a:
        print("yor are tied")
        print("play again")
    elif b=="s":
        if a=="g":
            print("you win")
        else:
            print("comp has win")
    elif b=="g":
        if a=="s":
            print("comp has win")
        else:
            print("you win")
    elif b=="w":
        if a=="s":
            print("you has win")
        else:
            print("comp has win")

print("comp turn:snake(s),gun(g)or Water(w)")
b= ""
randnum=random.randint(1,3)
if randnum==1:
    b=="s"
    b+="s"
elif randnum==2:
    b=="g"
    b+="s"
elif randnum==3:
    b=="w"
    b+="w"
a=input("you turn:snake(s),gun(g)or Water(w)")
gamewin(a,b)
print(f"you chose {a}")
print(f"comp chose {b}")