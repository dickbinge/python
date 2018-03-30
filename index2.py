print('这是中文吗?')
age=40
if age>=20:
	print('your age is %d'%age)
	print('adult')
elif age>=40:
	print('your age is %d'%age)
else:
	print('your age is too young!')
	print('----------------------')
	
#在python脚本运行的时候按回车到下一行不用按空格直接输入else,elif 即可
birth=input('birth:')
birth=int(birth)
if birth>2000:
	print('He is a 00后')
elif birth<1980:
	print('He is a 80前')
else:
	print('He is a young people')

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum1=0

#用for循环输出前100的和
def my_sum(n):
	sum=0
	for x in range(n+1):
		sum=sum+x
	print(sum)
	
#写一个求绝对值的方法
def my_abs(x):
	if not isinstance(x,(int ,float)):
		raise TypeError('This is a operand type')
		#当入参不是数值类型的视乎抛出自定义的异常
	if x>=0:
		return x
	else:
		return -x
		
