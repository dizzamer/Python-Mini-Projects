a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a1 > b1:
    a1, b1 = b1, a1
if b1 > a2:
    b1, a2 = a2, b1
if a1 > b2:
    a1, b2 = b2, a1
if a2 > b2:
    a2, b2 = b2, a2
else:
    print(b1, a2)
print(b1, a2)

