#1) Задание номер один
# A = int(input("Укажите целое число:"))
# B = int(input("Укажите целое число:"))
# while A <= B:
#     print("Условие задано правильно!!!")
#     break
# else:
#     print("Условие задано не правильно!!! Осталась 1 попытка")
#     A = int(input("Укажите целое число:"))
#     B = int(input("Укажите целое число:"))
# for i in range(A, B+1):
#     print(i)
##########################################################################
#2) Задание номер два
# A = int(input("Укажите целое число:"))
# B = int(input("Укажите целое число:"))
# while A <= B:
#     print("Условие задано правильно!!! A<=B ")
#     for i in range(A, B + 1):
#         print(i)
#     break
# else:
#     if A >= B:
#         print("Условие задано правильно!!! A>=B ")
#         for i in range(A, B - 1, -1):
#             print(i)
##########################################################################
#3) Задание номер три
# X = int(input("Укажите целое число:"))
# Y = int(input("Укажите целое число:"))
# day = 0
# while Y - X >= 0:
#     X *= 0,1
#     day += 1
# print(day)
# ##########################################################################
# #4) Задание номер четыре
# K = 0
# while int(input("Укажите целое число:")) != 0:
#     K += 1
# print(K)
# ##########################################################################
# #5) Задание номер пять
# a=int(input("Укажите целое число:"))
# b=int(input("Укажите целое число:"))
# K=0
# if B>A:
#     K+=1
# A=B
# while B!=0:
#     B=int(input("Укажите целое число:"))
#     if B>a:
#         K+=1
#     A=B
# print(K)
# ##########################################################################
# #6) Задание номер шесть
# a=int(input("Укажите целое число:"))
# b=int(input("Укажите целое число:"))
# if A>B:
#     max1=A
#     max2=B
# else:
#     max1=B
#     max2=A
# while B!=0:
#     B=int(input("Укажите целое число:"))
#     if B>max1:
#         max2=max1
#         max1=B
#     elif B>max2:
#         max2=B
# print(max2)
# ##########################################################################
# #7) Задание номер семь
# fib1 = 1
# fib2 = 1
#
# n = input("Номер ряда Фибоначчи: ")
# n = int(n)
#
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#
# print("Значение элемента:", fib2)
# ##########################################################################
# #8) Задание номер восемь
# p=int(input("Укажите целое число:"))
# c=1
# b=0
# while p!=0:
#     v=int(input())
#     p,v=v,p
#     if v==p:
#         c+=1
#     if c>b:
#         b=c
#     if p!=v:
#         c=1
# print(b)
# ##########################################################################
# #9) Задание номер девять
# n = input("Укажите число:").split()
# chet = []
# for i in range(len(n)):
#     n[i] = int(n[i])
#     if (i - 1) % 2 != 0:
#         chet.append(str(n[i]))
# print(' '.join(chet))
# ##########################################################################
# #10) Задание номер десять
# a = [int(s) for s in input().split()]
# for i in range(1,len(a)):
#     if a[i]>a[i-1]:
#         print(a[i])
# ##########################################################################
# #11) Задание номер одинадцать
# a = [int(s) for s in input("Укажите целое число:").split()]
# mx=a[0]
# mi=0
# for i in range(1,len(a)):
#     if a[i]>mx:
#         mx=a[i]
#         mi=i
# print(mx,mi)
# ##########################################################################
# #12) Задание номер двенадцать
# a = [int(i) for i in input("Укажите целое число:").split()]
# x = int(input("Укажите целое число:"))
# pos = 0
# while pos < len(a) and a[pos] >= x:
#     pos += 1
# print(pos + 1)
# ##########################################################################
# #13) Задание номер тринадцать
# a= [ 1, 2, 5, 0, 7, 3, 2 ]
# print( a )
#
# for i in range( 0, len( a ) - 1, 2 ):
#     a[ i ], a[i + 1] = a[i + 1], a[i]
#
# print( a )
# ##########################################################################
# #14) Задание номер цетырнадцать
# a = [{min(a): max(a), max(a): min(a)}.get(x, x) for x in a]
# ##########################################################################
# #15) Задание номер пятнцадать
# a = [7, 6, 5, 4, 3, 2, 1]
# k = 2
# result = a[:k] + a[k + 1:]
# print(result)
# ##########################################################################
# #16) Задание номер шестнадцать
# a=[int(i) for i in input().split()]
# k,c=[int(e) for e in input().split()]
# a.insert(k,c)
# a=(" ".join([str(i)for i in a]))
# print(a)
# ##########################################################################
# #17) Задание номер семьнадцать
# n = 8
# x = [0] * n
# y = [0] * n
# result = 'NO'
# for i in range(n):
#     x[i], y[i] = [int(j) for j in input().split()]
# for i in range (n):
#     for j in range(i+1,n):
#         if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
#             result = 'YES'
# print(result)
##########################################################################