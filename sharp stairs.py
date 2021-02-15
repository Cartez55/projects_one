import sys

count = int(sys.argv[1])

# for i in range(int(count)):
for i in range(count):
    while i != 0:
        print(i * '#')
        i -= i
