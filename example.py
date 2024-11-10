#single linked list-->
#create Node
#insert at beginning
#insert at ending
#insert at Specific Position
#Remove element 
#get length
#print LinkedList
# class Node:
#     def __init__(self,data):
#         self.data =data
#         self.next =None

# class singleLinkedList:
#     def __init__(self):
#         self.head =None
    
#     def insert_at_beginning(self,data):
#         if self.head==None:
#             node =Node(data)
#             self.head =node
#             return
#         else:
#             node=Node(data)
#             node.next =self.head
#             self.head = node
    
#     def show(self):
#         current =self.head

#         while current is not None:
#             print(current.data,end="-->")
#             current =current.next
#         print(None)

#     def insert_at_end(self,data):
#         if self.head ==None:
#             self.insert_at_beginning(data)
#             return
#         else:
#             current =self.head

#             while current.next is not None:
#                 current=current.next
            
#             node =Node(data)
#             current.next =node
                 
# singleL = singleLinkedList()
# singleL.insert_at_beginning(4)
# singleL.insert_at_beginning(7)
# singleL.insert_at_beginning(5)
# singleL.insert_at_end(10)
# singleL.insert_at_end(12)
# singleL.insert_at_beginning(20)
# singleL.show()



        