def mid(s=""):
    if len(s) % 2 == 0:
        return ""
    else:
        lungime = round(len(s)/2)-1
        mijloc = s[lungime]
        print(mijloc)
        return mijloc
mid("abc")