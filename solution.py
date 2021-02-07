import sys

ar = []
digit_string = sys.argv[1]
for i in digit_string:
    ar.append(int(i))
print(sum(ar))
