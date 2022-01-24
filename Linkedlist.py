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
    # Inserting at the end
    def insert_at_tail(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data,None)
    #Inserting values in the Linkedlist
    def insertValues(self,dataList):
        self.head=None
        for data in dataList:
            self.insert_at_tail(data)
        return
    # getting the length of the Linkedlist
    def countLength(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    # Removing an element in the LinkedList
    def removeAt(self,index):
        if index<0 or index>self.countLength():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
        count=0
        itr=self.head
        while itr:
            if count ==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    # inserting in between the LinkedList
    def insertAt(self,index,data):
        if index<0 or index>self.countLength():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_begining(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
#Creating LinkedList
"""ll=LinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(6)
ll.insert_at_begining(7)
ll.insert_at_begining(8)
ll.insert_at_begining(9)
ll.insert_at_begining(10)
ll.insert_at_tail(121)
ll.insert_at_tail(122)
ll.printList()"""
ll2=LinkedList()
ll2.insertValues([1,2,3,4,5])
ll2.removeAt(2)
ll2.insertAt(45,2)
ll2.printList()
print(ll2.countLength())