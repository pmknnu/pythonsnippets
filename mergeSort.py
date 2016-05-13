def mergeSort(alist):
	mid=len(alist)/2
	if len(alist)>1:
		left=alist[:mid]
		right=alist[mid:]
		mergeSort(left)
		mergeSort(right)
	
		i=0
		j=0
		k=0
		
		while i<len(left) and j<len(right):
			if left[i]<right[j]:
				alist[k]=left[i]
				i=i+1
			else:
				alist[k]=right[j]
				j=j+1
			k=k+1
		while i<len(left):
			alist[k]=left[i]
			i=i+1
			k=k+1
		while j<len(right):
			alist[k]=right[j]
			j=j+1
			k=k+1

		
alist=[4,2,1,3]
mergeSort(alist)
print alist