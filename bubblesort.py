def bubbleSort(alist):
	for j in range(len(alist)-1):
		for i in range(len(alist)-1):
			if(alist[i]>alist[i+1]):
				temp=alist[i]
				alist[i]=alist[i+1]
				alist[i+1]=temp

alist=[22,4,5,4,552,34,56]
bubbleSort(alist)
print alist
				