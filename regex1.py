# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
input=int(raw_input())
testCases=[]
while input:
    testCases.append(str(raw_input()))
    input-=1
print testCases	
for i in range(len(testCases)):
	pattern=r'^[+-]?\d*\.\d+$'
	print str(bool(re.search(pattern,testCases[i]))).lower()	