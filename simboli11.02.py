teikums = str()
atstarpe=1
teikums = input()
print(len(teikums))
print(teikums[0])
print(teikums[-2])
teikums.count("a")
teikums.count('A')
print(teikums.count("a")+teikums.count('A'))
print(teikums.count(" ")+1)
if teikums.find(" "):
    print(teikums.split()[0])
