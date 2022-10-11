# from random import randint

# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
#     koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
#     if k == 1:
#         ans.append(f'{koefs[i]}*x')
#     elif k == 0:
#         ans.append(f'{koefs[i]}')
#     else:
#         ans.append(f'{koefs[i]}*x**{k}')
#     flag = randint(0, 1)
#     if flag == 1:
#         ans.append('+')
#     elif flag == 0:
#         ans.append('-')
#     k -= 1

# ans.pop(-1)
# ans.append('=0')
# fout = open('output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()

# З1
# qnt = int(input("Input the number of decimal places: "))

# pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095

# pi_for_user = round(pi, qnt+1)

# for i in range(qnt):
#     pi_for_user *= 10

# pi_for_user = math.trunc(pi_for_user)

# while pi_for_user > 10:
#     pi_for_user /= 10

# print(round(pi_for_user, qnt))
# з2

# n = int(input("Введите число N: "))
# i = 2 
# list = []

# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")
# з3


# def elements(nums):
#     nums = [int(i) for i in nums.split()]
#     return list(set(nums))

# numbers = '1 1 2 2 3 455 66 66 2 1'
# print(elements(numbers))

# b = [1, 1, 2, 3, 3, 4, 5]
#  a = []
#  for i in b:
#     if b.count(i) == 1:
#          a.append(i)

#  print(a)

# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде
#  последовательности оставшихся чисел в одну строчку через пробел.

# arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
# print(list(filter(lambda e: 9 < e < 100, arr)))

# print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))

# st = '2 32 34 5 43 2 4 34'.split()
# res = list(filter(lambda x: len(x) == 2, st))
# print(res)


# 2. Дан список, вывести отдельно буквы и цифры.

# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')
 

# b= filter(str.isalpha, a)
# c= filter(str.isdigit, a)

# print(*b)
# print(*c)

# 3. Преобразовать набора списков 
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор 

# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]

# и потом вернуть в исходное состояние

# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# a,b,c = map(list,zip(users, ids, salary))
# print(a,b,c, sep="\n")
# a,b,c= map(list,zip(a,b,c))

# print(a,b,c, sep="\n")

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# for i in zip(users, ids, salary):
#     print(i)

# users_1, ids_1, salary_1 = map(list, zip(*zip(users, ids, salary)))

# print(users_1,ids_1,salary_1+ '\n')







