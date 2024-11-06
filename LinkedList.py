     
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node2.next = node3
# head = node1
# current =head
# while current is not None:
#     print(current.data,end='-->')
#     current=current.next

# print("None")

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        if self.head is None:
            node =Node(data)
            self.head=node
        else:
            node =Node(data)
            node.next =self.head
            self.head = node
    def show(self):
        current =self.head
        while current:
            print(current.data,end="-->")
            current = current.next
        
        print(None)
    
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head =Node(data)
            return
        current = self.head
        while current.next:
            current = current.next      
        current.next = Node(data)
    
    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        
        current = self.head
        count = 0

        while current:
            if count == index-1:
                node = Node(data,current.next)
                current.next=node
                break
            
            current = current.next
            count+=1
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head =self.head.next
            return
        
        current =self.head
        count = 0
        while current:
            if count == index-1:
                current.next = current.next.next
                break
                
            current=current.next
            count+=1
 
linkA = LinkedList()
linkA.insert_at_begining(5)
linkA.insert_at_begining(6)
linkA.insert_at_begining(7)
linkA.insert_at_end(5)
linkA.insert_at_end(6)
linkA.insert_at_end(7)
linkA.insert_at(2,12)
linkA.remove_at(1)

# linkA.show()
# print(linkA.get_length())


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None


# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#     def insert_at_begining(self,data):
#         if self.head is None:
#             new_node =Node(data)
#             self.head=new_node      
#         else:
#             new_node = Node(data)
#             new_node.next = self.head
#             new_node.prev=None
#             self.head=new_node
#     def insert_at_end(self,data):
#         if self.head is None:
#             new_node = Node(data)
#             self.head = new_node
#         else:
#             new_node = Node(data)           
#             current = self.head
#             while current.next:
#                 current =current.next
#             new_node.prev = current
#             current.next =new_node

#     def show(self):
#         current = self.head

#         while current:
#             print(current.data,end='-->')
#             current=current.next       
#         print(None)
    
#     def reverse(self):
#         temp =None
#         current =self.head

#         while current:
#             temp =current.prev
#             current.prev=current.next
#             current.next =temp
#             current =current.prev
#         if temp:
#             self.head =temp.prev
    
#     def insert_at(self,index,data):
#         if index<0 or index > self.length():
#             raise Exception("Invalid Index")
#         if index == 0:
#             self.insert_at_begining(data)
        
#         current = self.head
#         count = 0

#         while current:
#             if count == index-1:
#                 new_node =Node(data)
#                 new_node.prev =current
#                 new_node.next =current.next
#                 current.next.prev = new_node
#                 current.next=new_node       
#             current =current.next
#             count+=1
    

#     def length(self):
#         current =self.head
#         count=0
#         while current:
#             current=current.next
#             count+=1
#         return count
#     def remove_at(self,index):
#         if index<0 or index > self.length():
#             raise Exception("Invalid Index")
#         if index == 0:
#             self.head =self.head.next                
#         current = self.head
#         count = 0

#         while current:
#             if count == index-1:
#                 current.next=current.next.next
#                 current.next.next.prev=current
            
#             current =current.next
#             count+=1

# doubleA = DoubleLinkedList()
# # doubleA.insert_at_begining(3)
# # doubleA.insert_at_begining(4)
# # doubleA.insert_at_begining(5)
# doubleA.insert_at_end(5)
# doubleA.insert_at_end(6)
# doubleA.insert_at_end(7)
# doubleA.insert_at_end(8)
# doubleA.insert_at_end(9)
# doubleA.insert_at(3,10)
# # doubleA.remove_at(2)
# doubleA.reverse()
# doubleA.show()

# print(doubleA.length())
  