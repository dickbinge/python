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
