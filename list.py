firstList = ["Ball", "Athlete-tape", "Sneakers", "Gear", 'Athlete-tape']
secondList =  ["Net", "Athlete-tape", "paint", "Beam", 'Athlete-tape', "Antenna"]
thirdList = ["joji", "solomon", "Dceaser", "frankOcean",  "Giveon"]

i = len(firstList)
j = len(secondList)
k = len(thirdList)



print("This is a guessing game. ")
x = input(f"Enter an athlete essential, you have {len(firstList)} tries: ")



if x in firstList:
    y = input(f"Congratulations, next a couple of things you'd find on a Volleyball court, you have {len(secondList)} tries: ")

    if y in secondList:
        z = input(f"Well done, Finally guess a random RnB artist, you have {len(thirdList)} tries: ")    

        if z in thirdList:
            print("Cool! you finished the guessing game. ")
            
        else:
            k -= 1
            print(f"Try again, you have {k} tries /n Bruhh")
            if k == 0:
                print("Game over")
    else:
            j -= 1
            print(f"Try again, you have {j} tries")
            if j == 0:
                print("Game over")            
else: 
            i -= 1
            print(f"Try again, you have {i} tries")
            if i == 0:
                print("Game over")                
            
        