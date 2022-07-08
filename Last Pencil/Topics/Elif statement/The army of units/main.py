
b = range(1, 9 + 1)
c = range(10, 49 + 1)
d = range(50, 499 + 1)
e = range(500, 999 + 1)
f = range(1000, 1000000)
army_size = int(input())
if army_size < 1:
    print("no army")
elif army_size in b:
    print("few")
elif army_size in c:
    print("pack")
elif army_size in d:
    print("horde")
elif army_size in e:
    print("swarm")
elif army_size in f:
    print("legion")
