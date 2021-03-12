import matplotlib.pyplot as plt
import math
import sys



def Arg(z):
    if z.imag >= 0:
        phi = math.acos(z.real/math.sqrt(z.real**2 + z.imag**2))
    else:
        phi = -math.acos(z.real/math.sqrt(z.real**2 + z.imag**2))
    return phi


if len(sys.argv) > 1:
    z = complex(sys.argv[1])
    n = int(sys.argv[2])
else:
    z = 8
    n = 3

r = math.sqrt(z.real**2 + z.imag**2)
z_betrag = r**(1/float(n))

data_x = []
data_y = []
for k in range(n):
    phi = Arg(z)
    a = math.cos((phi+2*k*math.pi)/n)
    b = 1j * math.sin((phi+2*k*math.pi)/n)
    w_k = z_betrag * (a + b)

    data_x.append(w_k.real)
    data_y.append(w_k.imag)

fig, ax1 = plt.subplots()
ax1.scatter(data_x, data_y)

ax1.set(xlabel='Real', ylabel='Imag',
    title=f"{n} Wurzeln von: {z.real} + {z.imag}i")
ax1.grid()

print(f"{n}te Wurzeln von: {z.real} + {z.imag}i")
print()
for i, j in enumerate(data_x):
    print(f"{i+1}te Wurzel: {round(j, 3)} + i({round(data_y[i], 3)})")
plt.show()