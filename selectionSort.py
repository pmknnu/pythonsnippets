def selectionSort(alist):
	
	for k in range(len(alist)):
		min=k;
		for i in range(k,len(alist)):
			if alist[min]>alist[i]:
				min=i
				
		temp=alist[k]
		alist[k]=alist[min]
		alist[min]=temp
	
	 
alist=[63,23,88,45,67,88]     
selectionSort(alist)
print alist

