# dictionary=dict()
# dictionary[1]='ORANGE'
# print(dictionary)

# import calendar
#
# def leap(y):
#     if(calendar.isleap(y)):
#         return str(y)+" is a Leap year."
#     else:
#         return str(y) + "is not a Leap year."
#
# year=int(input("Enter Year :"))
# print(leap(year))


# c=45
# d=30
#
# # 2 variable
# # c=d+c
# # d=c-d
# # c=c-d
#
# # 3 variable
# temp=c
# c=d
# d=temp
# print(c,d)


# str1="anujsharma"
# rev=""
# for i in range(len(str1)-1,-1,-1):
#     rev+=str1[i]
# print(rev)




n=int(input())
space=n-1
count=1
for i in range(n,0,-1):
    print(" "*space +"*"*count)
    space-=1
    count+=2








