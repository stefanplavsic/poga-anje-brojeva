import random
ZBroj=random.randint(0,20)
brojpok=5
while brojpok>0:
    pitanje=int(input("unesite neki broj: "))
    if(pitanje==ZBroj):
        print("bravo,uspeli ste!:)")
        break
    else:
        print("kompjuter je zamislio broj ",ZBroj, "niste uspeli.:(")
        brojpok=brojpok-1
            
