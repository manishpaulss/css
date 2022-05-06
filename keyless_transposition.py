str = input("Eneter string: ")
n = int(input("Column size: "))
chunks = [str[i:i+n] for i in range(0, len(str), n)]

result = ""
for i in range(n):
    for word in chunks:
        try:
            result += word[i]
        except:
            pass
print(result)
