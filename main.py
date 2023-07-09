#1009 정수론 문제..
# import sys
# input = sys.stdin.readline
#
# sqrList = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6],
#            [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
#
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     a %= 10
#     ans = sqrList[a][b % len(sqrList[a]) - 1]
#     print(ans)

#1004
# import sys
# input = sys.stdin.readline
# import math
# sys.setrecursionlimit(10**7)
#
# T_num = int(input())
# arr=[]
#
#
# def check_in(x,y,r):
#     global start_in
#     global end_in
#     start_in =0
#     end_in =0
#     if r >= math.sqrt( (S_E[0]-x)**2 +(S_E[1]-y)**2 ) :
#         start_in=1
#     if r >= math.sqrt( (S_E[2]-x)**2 +(S_E[3]-y)**2 ) :
#         end_in = 1
#
# result=[0 for i in range (T_num)]
#
# for i in range(T_num):
#     S_E = list(map(int, input().split()))
#     C_num = int(input())
#     for j in range(C_num):
#         arr.append(list(map(int,input().split())))
#
#     for k in range(C_num):
#         check_in(arr[k][0],arr[k][1],arr[k][2])
#         if start_in == 0 and end_in == 0:
#             continue
#         elif start_in == 1 and end_in == 1:
#             continue
#         else:
#             result[i] += 1
#     arr = []
#
# for i in range(T_num):
#     print(result[i])

#1003
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
#
# arr = []
# case =[]
# for i in range(41):
#     line = [0,0]
#     arr.append(line)
# arr[0][0]=1
# arr[0][1]=0
# arr[1][0]=0
# arr[1][1]=1
# def fibonacci(num):
#     for i in range (2,num):
#         arr[i][0]=arr[i-1][0]+arr[i-2][0]
#         arr[i][1]=arr[i-1][1]+arr[i-2][1]
#
#
# fibonacci(41)
#
# Test_num = int(input())
#
# for i in range(Test_num):
#     case.append(int(input()))
#
# for i in range(Test_num):
#     print(arr[case[i]][0],end=" ")
#     print(arr[case[i]][1])



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