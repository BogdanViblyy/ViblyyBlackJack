from random import *

valet=10
dama=10
kuningas=10
tuz=11
bank=200
mangejakardid=[]
dillerikardid=[]
kardid=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,valet,valet,valet,valet,dama,dama,dama,dama,kuningas,kuningas,kuningas,kuningas,tuz,tuz,tuz,tuz]
kasmangloppenud=False
mangud=0
while bank>0:
    if mangud>0:  
        while True:
            try:
                vastus1=int(input("Kas tahad mängida veel? Jah-(1) Ei-(0): "))
                if vastus1==0 or vastus1==1:
                    break
                elif vastus1!=1:
                    print("Palun sissetage 1 või 2")
            except ValueError:
                print("Sissetage täisarv")
    else:           
        while True:
            try:
                vastus1=int(input("Kas tahad mängida BlackJack? Jah-(1) Ei-(0): "))
                if vastus1==0 or vastus1==1:
                    break
                elif vastus1!=1:
                    print("Palun sissetage 1 või 2")
            except ValueError:
                print("Sissetage täisarv")
        if vastus1==1:
            while True:
                try:
                    pakkumine=int(input("Sull on {} euro, kui palju sa tahad bettida: ".format(bank)))
                    if 0<pakkumine<=bank:
                        break
                    else:
                        print("Palun sissetage arv rohkem kui null ja väiksem või võrdne teie bankiga")
                except ValueError:
                    print("Sissetage täisarv")
            while len(mangejakardid)<2:
                randomkard1=choice(kardid)
                mangejakardid.append(randomkard1)
                kardid.remove(randomkard1)
                randomkard2=choice(kardid)
                dillerikardid.append(randomkard2)
                kardid.remove(randomkard2)
        
            while kasmangloppenud==False:
                while True:
                    try:
                        vastus2=int(input("Sull on: {}. Dilleril on {} ja veel üks kaard, kas tahat võtta veel ühe kardi(1) või ei(0): ".format(mangejakardid,randomkard2)))
                        if vastus2==1 or vastus2==0:
                            break
                        else:
                            print("Palun sissetage 1 või 2")
                    except ValueError:
                        print("Sissetage täisarv")
                if vastus2==1:
                    randomkard3=choice(kardid)
                    kardid.remove(randomkard3)
                    mangejakardid.append(randomkard3)
                    while sum(mangejakardid)<=21:
                        while True:
                            try:
                                vastus3=int(input("Nüüd sull on {}, kas tahad võtta veel? Jah-(1) Ei-(0): ".format(mangejakardid)))  
                                if vastus3==1 or vastus3==0:
                                    break
                                else:
                                    print("Palun sissetage 1 või 2")
                            except ValueError:
                                print("Sissetage täisarv")
                        if vastus3==1:
                        
                            randomkard3=choice(kardid)
                            kardid.remove(randomkard3)
                            mangejakardid.append(randomkard3)
                        else:      
                            kasmangloppenud=True          
                    else:
                        kasmangloppenud=True
                else:
                    kasmangloppenud=True
        else:
            print("Vale vastus")
    while tuz in mangejakardid and sum(mangejakardid)>21:
        tuz=1

    if kasmangloppenud==True: 
       mangud+1
       while sum(mangejakardid)>sum(dillerikardid) and sum(dillerikardid)<17:
            randomkard=choice(kardid)
            kardid.remove(randomkard)
            dillerikardid.append(randomkard)
       print("Dillerikaardid", dillerikardid)
       voit=pakkumine*2
       if sum(mangejakardid)>sum(dillerikardid) and sum(mangejakardid)<22:
           print("Te võidsite",voit," euro!")
           bank=voit+bank
       elif sum(mangejakardid)>sum(dillerikardid) and sum(mangejakardid)>22:
           print("Te kaotasite",pakkumine,"euro, sest teil on rohkem kui 21")
           bank=bank-pakkumine
       elif sum(mangejakardid)<sum(dillerikardid) and sum(mangejakardid)<22:
           print("Te kaotasite",pakkumine,"euro")
           bank=bank-pakkumine
       elif sum(mangejakardid)<sum(dillerikardid) and sum(dillerikardid)>22:
           print("Te võidsite",voit," euro!")
           bank=voit+bank
       elif sum(mangejakardid)==sum(dillerikardid):
           print("Draw")
else:
    print("Sa kaotasid kõik sinu raha, sa oled ludoman!")



