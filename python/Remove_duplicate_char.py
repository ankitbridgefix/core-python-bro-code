string = "ABCDEDFASDFDADSAEDD"
d = ""
for chr in string:
    if chr not in d:
        d+=chr
else:
    print(d)