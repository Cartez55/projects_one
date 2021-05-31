# kata - https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

def tickets(people):
    # print(people[-2])
    for index in range(0, len(people)):
        if people[index] == 50 or 100:
            int(people[index]) - 25
            if len(people) <= 3:
                if int(people[-1]) // 2 == 25:
                    print("YES")
                else:
                    print("NO")
            else:
                print(int(people[index]) + int(people[-2]))
                if int(people[index]) + int(people[-2]) == int(people[-1]) - 25:
                    print("YES")
                else:
                    print("NO")


tickets(([25, 25, 50]))