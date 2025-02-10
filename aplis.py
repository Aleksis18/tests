Ax=int(input("Ievadi x:"))
Ay=int(input("Ievadi y:"))
radiuss=int(input("Ievadi radiusu:"))
attalums=(Ax-0)**2+(Ay-0)**2
import math
attalums1=(math.sqrt(attalums))
if attalums1<=radiuss:
    print("Ieksa rinka linija")
if attalums1>radiuss:
    print("Arpus rinka linijas")



