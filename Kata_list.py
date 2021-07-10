# kata - https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

def tickets(people):
    balance = []
    short_change = []
    result_balance = []

    try:
        for index in range(0, len(people)):
            if people[index] < 0:
                return ('NO-отрицательное')
            if people[index] > 25:
                short_change.append(people[index])
            else:
                balance.append(people[index])
        # print(f"balance: {balance} | short_change : {short_change}")

        for cash in range(0, len(short_change)):
            if (short_change[cash] - balance[cash]) < 0:
                break
            else:
                result_balance.append(short_change[cash] - balance[cash])
                result_balance.extend(balance)
                del balance[len(result_balance)]
        # print(f"result_balance: {result_balance} | short_change : {short_change}")

        if sum(result_balance[0:-1]) == (result_balance[-1]) or result_balance[-2] == result_balance[-1]:
            return ('YES')
        else:
            return ('NO-условие2')
    except:
        return ('NO-ошибка')

    # if len(people) <= 3:
    #     if int(people[-1]) // 2 == 25:
    #         return("YES")
    #     else:
    #         return("NO")
    # else:
    #     return(int(people[index]) + int(people[-2]))
    #     if int(people[index]) + int(people[-2]) == int(people[-1]) - 25:
    #         return("YES")
    #     else:
    #         return("NO")


# def tickets(people):
#     for index in range(0, len(people)):
#         try:
#             if people[index] > 0:
#                 if people[index] == 50 or people[index] == 100:
#                     int(people[index]) - 25
#                     if len(people) <= 3:
#                         if int(people[-1]) // 2 == 25:
#                             return ("YES")
#                         else:
#                             return ("NO")
#                     else:
#                         if int(people[index]) + int(people[-2]) == int(people[-1]) - 25:
#                             return ("YES")
#                         else:
#                             return ("NO")
#             else:
#                 return ("NO")
#         except:
#             return ("NO")
#
# tickets(([25, 25, 50]))
print(tickets(([25, 25, 50])))
