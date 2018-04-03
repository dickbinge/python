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


#create by Jingbin  2018/4/3
