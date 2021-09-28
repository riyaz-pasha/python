s=input()

alphas=""
specialsChars=""

for i in s:
    if i.isnumeric():
        continue
    elif i.isalpha():
        alphas+=i
    else:
        specialsChars+=i

print(alphas,specialsChars)