#1267
# T_num = int(input())
#
# Y_sum=0
# M_sum=0
# arr=list(map(int,input().split()))
# count_Y=0
# count_M=0
#
#
# for i in range(T_num):
#     money_Y = arr[i]
#     money_M = money_Y
#
#     while money_Y > 0:
#         if money_Y ==30:
#             count_Y+=1
#         money_Y = money_Y - 30
#         count_Y += 1
#
#     Y_sum += count_Y*10
#
#     while money_M > 0:
#         if money_M == 60:
#             count_M += 1
#         money_M = money_M - 60
#         count_M +=1
#
#     M_sum += count_M*15
#
#     count_Y =0
#     count_M =0
#
# if M_sum == Y_sum :
#     print("Y", "M", Y_sum)
# elif M_sum > Y_sum :
#     print("Y", Y_sum)
# else  :
#     print("M" ,M_sum)
#1259
# num = []
# num=input()
# while num !="0":
#     imsi=num[::-1]
#     if num==imsi:
#         print("yes")
#     else :
#         print("no")
#
#     num=input()
# 1247
# for z in range(3):
#     N = int(input())
#     sum = 0
#     for i in range(N):
#         sum += int(input())
#
#     if sum == 0:
#         print(0)
#     elif sum > 0:
#         print("+")
#     else:
#         print("-")
#1157


# abc= input()
# ac= abc.upper()
# word=(list(ac))
# abc=[]
# arr= dict(list())
# for i in range(len(word)):
#     N=word[i]
#     if N not in abc:
#         abc.append(N)
#         arr[N] = 1
#     else :
#         arr[N] += 1
#
# result = sorted(arr.items(), key=lambda x:x[1] , reverse=True)
#
# if len(result) != 1:
#     if result[0][1] != result[1][1] :
#         print(result[0][0])
#     else:
#         print("?")
# else:
#     print(result[0][0])
#1141

# NUM = int(input())
# count = 0
# arr=[]
#
# for i in range(NUM):
#     arr.append(input())
#
# arr.sort(key=len)
#
#
# for i in range(NUM):
#     nowWord = arr[i]
#     flag = 0
#     for j in range (i+1,NUM):
#         nextword=arr[j]
#         if nextword.find(nowWord) == 0:
#                 flag=1
#                 break
#         else:
#             continue
#     if flag != 1:
#         count += 1
# print(count)
#1107

# target = int(input())
# ans = abs(100 - target)
# M = int(input())
# if M:
#     broken = set(input().split())
# else:
#     broken = set()
#
#
#
# for num in range(1000001):
#     for N in str(num):
#         if N in broken:
#             break
#     else:
#         ans = min(ans, len(str(num)) + abs(num - target))
#
# print(ans)

#1085

# x,y,w,h=map(int,input().split())
#
# arr=[]
# arr.append(x)
# arr.append(y)
# arr.append(w-x)
# arr.append(h-y)
# arr.sort()
#
# print(arr[0])
#


# #11050
# import math
#
# n,k=map(int,input().split())
# a=math.factorial(n)
# b=math.factorial(n-k)
# c=math.factorial(k)
# print(int(a/(b*c)))
#
#
#
# arr=list(map(str,input().split()))
#
# print(len(arr))

#1065
#
# num= int(input())
# result = 99
# count =0
# real=num
# num_s=num
#
# while num !=0:
#     num = num // 10
#     count +=1
#
# if count ==1 or count ==2:
#     print(num_s)
# elif count==4:
#     print(144)
# else:
#     for i in range(100,real+1):
#         zxc=i
#         one = zxc % 10
#         zxc = zxc //10
#         ten = zxc % 10
#         zxc = zxc //10
#         hundred = zxc % 10
#         diff1=one-ten
#         diff2=ten-hundred
#         if diff1==diff2:
#             result+=1
#
#     print(result)

#1064
# import math
# ax,ay,bx,by,cx,cy=map(int,input().split())
#
#
#
# result=[]
#
# def check_sqr(ax,ay,bx,by,cx,cy):
#     if ax!=bx:
#         m=(ay-by)/(ax-bx)
#         if ay == m * (ax - cx) + cy:
#             print(-1.0)
#             return
#     elif ax!=cx:
#         m=(ay-cy)/(ax-cx)
#         if ay == m * (ax - bx) + by:
#             print(-1.0)
#             return
#     elif cx!=bx:
#         m=(cy-by)/(cx-bx)
#         if by == m * (bx - cx) + cy:
#             print(-1.0)
#             return
#     elif ax==bx and bx==cx:
#         print(-1.0)
#         return
#
#     a_b = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
#     a_c = math.sqrt((ax - cx) ** 2 + (ay - cy) ** 2)
#     b_c = math.sqrt((bx - cx) ** 2 + (by - cy) ** 2)
#     arr=[a_b,a_c,b_c]
#     cha2 = max(arr)-min(arr)
#     print(2*cha2)
#
# check_sqr(ax,ay,bx,by,cx,cy)

#1012
# from collections import deque
#
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
#
# t = int(input())
#
# def bfs(graph, a, b):
#     queue = deque()
#     queue.append((a,b))
#     graph[a][b] = 0
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx < 0 or nx >=n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))
#
# for i in range(t):
#     cnt = 0
#     n, m, k = map(int,input().split())
#     graph = [[0]*m for _ in range(n)]
#
#     for j in range(k):
#         x, y = map(int, input().split())
#         graph[x][y] = 1
#
#     for a in range(n):
#         for b in range(m):
#             if graph[a][b] == 1:
#                 bfs(graph, a, b)
#                 cnt += 1
#     print(cnt)
#1018
# import sys,math
# input = sys.stdin.readline
# sys.setrecursionlimit(10*7)
# arr=[]
# result=[]
# M,N=map(int,input().split())
#
# for i in range(M):
#     arr.append(input())
#
# for i in range(M-7):
#     for j in range(N - 7):
#         chess1=0 #B
#         chess2=0 #W
#         for a in range(i,i+8):
#             for b in range(j,j+8):
#                 if (a+b)%2==0:
#                     if arr[a][b]=='B':
#                         chess2 += 1
#                     elif arr[a][b] == 'W':
#                         chess1 += 1
#                 else:
#                     if arr[a][b]=='B':
#                         chess1 += 1
#                     elif arr[a][b] == 'W':
#                         chess2 += 1
#         result.append(chess1)
#         result.append(chess2)
#
# print(min(result))

# 1011
# import sys,math
# input = sys.stdin.readline
# sys.setrecursionlimit(10*7)
#
# T_num=int(input())
#
# for i in range(T_num):
#     x,y=map(int,input().split())
#     distance = y-x
#     count = 0
#     move = 1
#     move_plus = 0
#     while move_plus < distance:
#         count += 1
#         move_plus += move
#         if count % 2 == 0:
#             move += 1
#     print(count)
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