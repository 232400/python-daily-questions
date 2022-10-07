str=["12345"]
n={}
for i in str:
    w="".join(sorted(i))
    if w in n:
        n[w].append(i)
    else:
        n[w]=[i]
print(n)
