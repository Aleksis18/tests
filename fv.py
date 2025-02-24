teikums = input()
vardi = teikums.split(" ")
for vards in vardi:
        if len(vards) == 3:
            print("IR 3 SIMBOLI")
            break
        if len(vards) != 3:
            print("NAV 3 SIMBOLI")

for vards in vardi:
    for i in range (len(vards)):
        if len(vards) == 3:
            print(vards,end=" ")
            break   

nr=0
for vards in vardi:
    for i in range(len(vards)):
        nr +=1
        if len(vards)%2==0:
            print(nr, end=" ")
            break
        
