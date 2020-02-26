import random
def getRandomArray(n):
	arr=[]
	randnum = random.randint(0, 1000000)
	for x in range(n):
    		while(randnum in arr):
        		randnum = random.randint(0, 1000000)
    	arr.append(randnum)
	print(arr)
def getSortedArray(n):
	arr = []
	for x in range(n):
    		arr.append(n-x-1)
	print(arr)