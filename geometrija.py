xkord1 = int(input())
ykord1 = int(input())
xkord2 = int(input())
ykord2 = int(input())
xkord3 = int(input())
ykord3 = int(input())
mala1=(xkord1-xkord2)**2+(ykord1-ykord2)**2
mala2=(xkord1-xkord3)**2+(ykord1-ykord3)**2
mala3=(xkord3-xkord2)**2+(ykord3-ykord2)**2

if mala1>mala2 and mala1>mala2:
    garais=mala1
    isais1=mala2
    isais2=mala3
elif mala2>mala1 and mala2>mala3:
    garais=mala2
    isais1=mala1
    isais2=mala3
else:
    garais=mala3
    isais1=mala2
    isais2=mala1
if garais==isais1+isais2:
    print("Veido taisnlenka trijsturi")
else:
    print("Nav")
