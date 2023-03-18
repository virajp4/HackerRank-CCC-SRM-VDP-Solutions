import math
import cmath

ab = int(input())
bc = int(input())

z = complex(bc/2,ab/2)
print(round(math.degrees(cmath.phase(z))),chr(176),sep='')