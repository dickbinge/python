#求x的平方
def power(x):
	return x*x
#求x的n次幂
def power1(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
#求x的n次幂,递归方法
def power2(x,n):
	s=1
	if n==1:
		s=x
	else:
		s=power2(x,n-1)*x
	return s

#求一组数的乘积
def product(*num):
	sum=1
	for n in num:
		sum=sum*n
	return sum

#打印学生信息
def enroll(names,sex,age=6,address='BeiJing'):
	print('nmaes:',names)
	print('sex:',sex)
	print('age:',age)
	print('address:',address)

#调用 ：enroll('jingbin','男')  前两个为必须参数，后两个默认参数

#可变参数 求 a*a+b*b+c*c...的值
def calc(*num):
	sum=0
	for n in num:
		sum=sum+n*n
	return sum
#调用  calc(1,3,5,6,3)

#关键字参数
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

extra={'address':'BeiJing','job':'Enginner'}
#调用上述函数
person('jingbin',43,**extra)

def person(name,age,**kw):
	if 'city' in kw:
		#有city参数
		pass
	if 'job' in kw:
		#有 job 参数
		pass
	print('name:',name,'age:',age,'other:',**kw)

# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict。

#汉诺塔问题
''' a,b,c 表示有三个柱子,将n个铜片由a移动到c
 n 表示当前的铜片数
'''
def hannuo(n,a,b,c):
	if n:
		hannuo(n-1,a,c,b)
		print('%s-->%s' %(a,c))
		hannuo(n-1,b,a,c)


#汉诺塔问题
m=0
def move(disk,start,end):
	print('第%s次移动:%d号圆盘由%s-->%s' %(++m,disk,start,end))
def hanoi(n,a,b,c):
	if n==1:
		move(1,a,c)
	else:
		hanoi(n-1,a,c,b)
		move(n,a,c)
		hanoi(n-1,b,a,c)

#切片 相当于slice函数
L=['Mick','Mary','Jack','Tom','Pery']
r=L[0:3] #表示从索引0开始取3个值
q=L[-2:-1] #倒序取值

L=list(range(100))  #含有前100的数组

L[:10]  #前10个数
L[-10:] #取后10个数
L[10:20] #取10~20
L[-20:-10] #取80~90
L[10:20:2] #间隔2取数
L[-10::5] #间隔5取数
L[:10:4]  #间隔4取数
L[:] #完全复制一个数组

#去除前后空格
def trim(str):
	while str[:1]=='':
		str=str[1:]
	while str[-1:]=='':
		str=str[:-1]
	return str

#使用迭代查找一个list中的最大最小值，并返回一个tuple
def findMinAndMax(L):
	if len(L)==0:
		return (None,None)
	else:
		min=L[0]
		max=L[0]
		for x in L:
			if min>x:
				min=x
			if max<x:
				max=x
		return (max,min)
#再回顾一下typle ：没有任何修改的方法(例如 push,add，pop，remove) ,定义出来里边值就是固定的


#列表生成器

list(range(1,11))  #1~10

#传统的写法
L=[]
for x in range(1,11):
	L.append(x*x)   #1~10平方

#列表生成器的写法

[x*x for x in range(1,11)] 

[x*x for x in range(1,11) if x%2==0]

[m+n for m in 'abc' for n in 'ABC'] #组合

#列出当前目录下的所有文件

import os  #导入os模块
[d for d in os.listdir('.')] #os.listdir可以列出当前目录下的所有文件名称

#create by Jingbin  2018/4/3
