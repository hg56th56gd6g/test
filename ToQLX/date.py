#-*- coding:utf-8 -*-
MonthToDayCount=[31,28,31,30,31,30,31,31,30,31,30,31]#储存了每个月对应的天数
#输入
year=  int(input("输入年: "))
month= int(input("输入月: "))
day=   int(input("输入日: "))
#检查月份是否合法
if not 1<=month<=12:
    print("不正确的月")
    exit()
#检查闰年
if year%4 == 0:
    print("是闰年")
    #将2月的天数+1
    MonthToDayCount[1] += 1
#检查日期是否合法
if not 1<=day<= MonthToDayCount[month-1]:
    print("不正确的日期")
    exit()
#将前面月的天数累加,这个函数将参数1里所有数相加,最后再加上参数2
count=sum(MonthToDayCount[:month-1:],day)
print("{}年{}月{}日是此年的第{}天".format(year,month,day,count))