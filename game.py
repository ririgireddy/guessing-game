a=int(input("Pick a number from 1 to 100: "))

b=random.randint(1, 100)

while a!=b:
    if a>b:
        print("guess lower")
        a=int(input("Pick a number from 1 to 100: ""))
    elif a<b:
        print("guess higher")
        a=int(input("Pick a number from 1 to 100: "))
    else:
        print("ey good job (the hint was to first guess 50 btw)")
