#if else statments
print("====example01====")
a = 3
b = 2
if a < b:
    print("a is less than b")
    print("a is defenitely less than b")
print("not sure if a is less than b")

print("====example02====")
c = 2
d = 4
if c < d:
    print("c is less than d")
else:
    print("c is NOT less than d")
    print("I don't think c is less than d")
print("outside the if block")

print("====example03====")
e = 9
f = 8
if e < f:
    print("e is less than f")
elif e == f:
    print("e is equal to f")
else: 
    print("e is greater than f")

print("====example04====")
g = 24
h = 8
if g < h:
    print("g is less than h")
else:
    if g > h + 15:
        print("g is grater than h by more 15")
    else:
        print("g is greater than h but not by more 15")
