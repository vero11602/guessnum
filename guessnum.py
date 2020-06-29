import random
count = 0
low = input ('請決定數值最小範圍:')
low = int (low)
high = input ('請決定數值最大範圍:')
high = int (high)
r = random.randint (low , high)
while True :
	count+=1 #count = count + 1 
	num = input ('請輸入數字:')
	num = int (num)
	if num == r :
		print ('終於猜對了')
		print ('總共猜了' ,count , '次')
		break
	elif num < r :
		print ('比答案大')
	elif num > r :
		print ('比答案小')

		

