class Node():
	def __init__(self,data=None,next=None):
		self.data=data
		self.next=next
	
def printList(head):
	while head!=None:
		print head.data
		head=head.next

def printReverse(head):
	if head!=None:
		printReverse(head.next)
		print head.data
		
def insertLast(head,data):
	temp=Node(data)
	
	print head.data
	if head.data==None:
		head=temp
		return head
	
	else:
		while(head.next!=None):
			head=head.next
		
		head.next=temp
	
	
		
		
				
	

node1=Node()
#node2=Node(2)
#node3=Node(3)
#node1.next=node2
#node2.next=node3
#printList(node1)
#printReverse(node1)
insertLast(node1,4)
printList(node1)