class Node:
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
# Starting in the beginning
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
#function for printing of Linkedlist
    def printList(self):
        if self.head is None:
            print("Sorry LinkedList is Empty")
            return
        else:
            itr=self.head
            llstr=''
            while itr:
                llstr+=str(itr.data)+'---->'
                itr=itr.next
            print(llstr)
#Creating LinkedList
ll=LinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(6)
ll.insert_at_begining(7)
ll.insert_at_begining(8)
ll.insert_at_begining(9)
ll.insert_at_begining(10)
ll.printList()



