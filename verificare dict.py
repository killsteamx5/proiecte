def online_count(dic):
    online = 0
    for x in dic:
        if dic[x] == "online":
            online += 1
    print(online)
    return online


online_count({"Alice": "online"})
