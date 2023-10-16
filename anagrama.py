def is_anagram(a, b):
    c = []
    d = []
    alf = "abcdefghijklmnopqrstuvwxyz"
    for x in a:
        c.append(alf.index(x))
    for y in b:
        d.append(alf.index(y))
    c.sort()
    d.sort()
    print(c)
    print(d)
    if c == d:
        return True
    else:
        return False


is_anagram("typhoon", "opython")
