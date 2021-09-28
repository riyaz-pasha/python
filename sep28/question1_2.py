import re

txt = input()
alphas = re.findall("[a-zA-Z]", txt)
specialsChars = re.findall("[^a-zA-Z0-9]", txt)

print("".join(alphas),"".join(specialsChars))