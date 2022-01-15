N = int(input())
words = []

for i in range(N):
    word = input()
    if word in words:
        continue
    else:
        words.append(word)

words.sort(key=lambda x : (len(x), x))

for word in words:
    print(word)
