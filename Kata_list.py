# kata - https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

def tickets(people):
    balance = []
    short_change = []
    result_balance = []

    try:
        for index in range(0, len(people)):
            if people[0] > 25:
                print('NO')
            if people[index] == 50 or people[index] == 100:
                short_change.append(people[index])
            elif people[index] < 0:
                print('NO')
            else:
                balance.append(people[index])
            if len(short_change) > len(balance):
                print('NO')
        print(f"balance: {balance} | short_change : {short_change}")

        for cash in range(0, len(short_change)):
            del balance[0]
            if (short_change[cash] - balance[cash]) < 0:
                break
            else:
                result_balance.append(short_change[cash] - balance[cash], balance)
        print(f"result_balance: {result_balance} | short_change : {short_change}")

        if sum(balance[0:-1]) == (balance[-1]) or balance[-2] == balance[-1]:
            print('YES')
        else:
            print('NO')
    except:
        print('NO')


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


# def tickets(people):
#     for index in range(0, len(people)):
#         try:
#             if people[index] > 0:
#                 if people[index] == 50 or people[index] == 100:
#                     int(people[index]) - 25
#                     if len(people) <= 3:
#                         if int(people[-1]) // 2 == 25:
#                             print ("YES")
#                         else:
#                             print ("NO")
#                     else:
#                         if int(people[index]) + int(people[-2]) == int(people[-1]) - 25:
#                             print ("YES")
#                         else:
#                             print ("NO")
#             else:
#                 print ("NO")
#         except:
#             print ("NO")
#
tickets(([25, 25, 100]))
