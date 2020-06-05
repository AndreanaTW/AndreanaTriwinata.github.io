a=2
for x in range(10):
    b = a - ((a**3-3*a**2-13*a+15)/(3*a**2-6*a-1))
    if a**3-3*a**2-13*a+15 != 0:
        a=b
    else:
        print("Akar adala", b)
        break
    print("Akar pers adala", b)
