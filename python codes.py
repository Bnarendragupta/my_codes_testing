"""1)fabonacci series"""
# n=int(input("enter the number:"))
# n1=0
# n2=1
# count=2

# if n<0:
#     print("give postive numbers")
# elif n<2:
#     print(n,end=" ")
# else:
#     print(n1,end=" ")
#     print(n2,end=" ")
#     while count<n:
#         n3=n1+n2
#         print(n3,end=" ")
#         count+=1
#         n1=n2
#         n2=n3
"""2)factorial"""

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))
"""3)prime number"""

# def check_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             print("not a prime")
#             break
#     else:
#         print("prime")
# check_prime(15)

"""4)valid anagram """
# a="amma"
# b="aamm"
# if len(a)!=len(b):
#     print("not valid")
# else:
#     if sorted(a)==sorted(b):
#         print("valid")
#     else:
#         print("not valid")

"""5)leap year"""
# def check_leapyear(n):
#     if n%4==0 and n% 100!=0 or n%400==0:
#         print("leap year")
#     else:
#         print("not leap year")
# check_leapyear(2001)

"""6)find the missing element in list"""
# l=[1,2,3,4,5,6,8,9]
# res=[ele for ele in range(max(l)+1) if ele not in l]
# print("missing element",str(res))

"""7)remove vowels from string"""
# str="narendra"
# vowels="aeiou"
# for i in str:
#     if i in vowels:
#         str=str.replace(i,"")
# print(str)

"""8)string reverse"""
# s="narendra"
# str=""
# for i in s:
#     str=i+str
# print(str)

"""9)change the string postion """
# s="harman"
# a=s[3:]+s[0:3]
# print(a)

"""10)count str number of alphabet and digits"""
# str="narendra9491"
# s=0
# for i in str:
#     if (i.isdigit()):
#         s+=1
# print("number of alphabets",len(str)-s)
# print("number of digits",s)

"""11)palindrom"""
# num="amma"
# if num == num[::-1]:
#     print("palindrom")
# else:
#     print("not palindrom")

"""12)reverse of word in string"""
# s="lets take leet code contest"
# a=" ".join(map(lambda word:word[::-1],s.split()))
# print(a)

"""13)count number of word present in list """
# l=['a','a','a','b','b','c','b','a','b','c']
# freq={}
# for i in l:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
#     print(freq)

"""14)decimal to binary"""
# d=10
# b=""
# while d>0:
#     r=d%2
#     b=str(r)+b
#     d=d//2
# print(b)

"""15)binary to decimal"""
# b="0101"
# d=0
# p=0
# for i in reversed(b):
#     if i=="1":
#         d=d+2**p
#     p=p+1
# print(d)

"""16)"""
    