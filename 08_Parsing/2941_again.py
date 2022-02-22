c_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for c_alpha in c_alphabets:
    if c_alpha in word:
        word = word.replace(c_alpha, '*')

print(len(word))