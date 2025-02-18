teikums=input()
vardi=teikums.split(" ")
vardu_nr=0
for vards in vardi:
    vardu_nr += 1
    druk_sk = 0
    for i in range(len(vards)):
        if vards[i]>='A' and vards[i]<='Z':
            druk_sk +=1
    if druk_sk == len(vards):
        print(vardu_nr)