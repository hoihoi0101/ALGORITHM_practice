#9020
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# def is_prime_number(x):
#     # 2부터 (x - 1)까지의 모든 수를 확인하며
#     for i in range(2, x):
#         # x가 해당 수로 나누어떨어진다면
#         if x % i == 0:
#             return False # 소수가 아님
#     return True # 소수임
#
# T_num = int(input())
# arr =[]
# answer_a=[]
# answer_b=[]
# for i in range(T_num):
#     arr.append(int(input()))
#
# for i in range(T_num):
#     a = int(arr[i] / 2 )
#     b = int(arr[i] / 2 )
#     while 1 :
#         if is_prime_number(a) and is_prime_number (b) :
#             answer_a.append(a)
#             answer_b.append(b)
#             break
#         a-=1
#         b+=1
#
# for i in range(T_num):
#     print(answer_a[i], end=" ")
#     print(answer_b[i])


# 2577
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
#
# num = 1
# for _ in range(3):
#     num = num * int(input())
#
#
# arr = [0 for i in range(10)]
#
# while num >0 :
#     index = num %10
#     num = num //10
#     arr[index]+=1
# for i in arr:
#     print(i)


# 25305
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
#
# total, index = map(int, input().split())
#
# arr = list(map(int, input().split()))
#
# arr.sort()
#
# print(arr[total-index])