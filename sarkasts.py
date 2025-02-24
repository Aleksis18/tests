teikums = input()
vardi = teikums.split(" ")
saraksts = vardi
saraksts.insert(2, "Sveiks")
saraksts.sort(reverse=True)
print(saraksts)