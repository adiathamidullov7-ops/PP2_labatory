def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1
    
ctr = fun(5)
for n in ctr:
    print(n)


def fibonachi(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

#Using
for num in fibonachi(10):
    print(num)




def countdown(n):
    while n>0:
        yield n
        n = -1

gen = countdown(5)
iterator = iter(gen)

print(next(iterator))
print(next(iterator))

def uniform_motion(v, t_max, dt=1):
    t = 0
    while t <= t_max:
        s = v * t
        yield t, s
        t += dt

for i, j in uniform_motion(10, 5):
    print(f"t={i} s, s={j} m")


def ohms_law(voltage_list, resistance):
    for u in voltage_list:
        yield u
        u / resistance
    
voltages = [5, 6, 7, 8, 9]
for u, i in ohms_law(voltages, 6):
    print(f"U = {U} V  I={i}  ")


def electric_power(voltage, current):
    for u, i in zip(voltage, current):
        P = u * i
        yield P

a, b = map(int, input())
for u, i, p in electric_power(a, b):
    print(p)

        