# kata - https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

def tickets(people):
    # print(people[-2])
    balance = []
    short_change = []
    for index in range(0, len(people)):
        if people[index] == 50 or people[index] == 100:
            short_change.append(people[index])
        else:
            balance.append(people[index])
    print(f"balance: {balance} | short_change : {short_change}")

    for cash in range(0, len(balance)):
        for pocket_money in range(0, len(short_change)):
            short_change.append(short_change[pocket_money] - 25)
            balance.append(short_change[pocket_money] - balance[cash])
    print(f"balance: {balance} | short_change : {short_change}")

    # list_bank.append(int(people[index]) - 25)
#
#     # if len(people) <= 3:
#     #     if int(people[-1]) // 2 == 25:
#     #         print("YES")
#     #     else:
#     #         print("NO")
#     # else:
#     #     print(int(people[index]) + int(people[-2]))
#     #     if int(people[index]) + int(people[-2]) == int(people[-1]) - 25:
#     #         print("YES")
#     #     else:
#     #         print("NO")
#
#
tickets(([25, 25, 50, 100]))
