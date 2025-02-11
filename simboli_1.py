teikums = str()
teikums = input()
if teikums[-1] == ".":
    print("Stastijuma teikums")
if teikums[-1] == "!":
    print("Izsaukuma teikums")
if teikums[-1] == "?" :
    print("Jautājuma teikums")
print(len(teikums))
for i in range(len(teikums)):
    if teikums[i]==' ':
        print(teikums[i-1])
print(teikums[-2])

