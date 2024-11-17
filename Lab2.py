# # TASK 1
# class Node:
#     def __init__(self,data):
#         self.color = data
#         self.next = None
    
#     def createList(array):
#         print(array)


# def createList(array):
#     head =None
#     for i in array:
#         if head ==None:
#             node =Node(i)
#             head = node
#         else:
#             current =head
#             while current.next is not None:
#                 current =current.next
            
#             node =Node(i)
#             current.next =node
    
#     return head


# def printLinkedList(head):
#     current =head

#     while current is not None:
#         print(current.color,end="-->")
#         current=current.next
    
#     print(None)

# def check_similar(build1,build2):

#     current_one =build1
#     current_two =build2

#     while current_one and current_two:
#         if current_one.color != current_two.color:
#             return  "Not Similar"
#         current_one =current_one.next
#         current_two =current_two.next
#     if current_one is None and current_two is None:
#         return "Similar"
#     else:
#         return "Not Similar"

# import numpy as np

# print('==============Test Case 1=============')
# building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
# building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
# print('Building 1: ', end=' ')
# printLinkedList(building_1)
# print('Building 2: ', end=' ')
# printLinkedList(building_2)
# returned_value = check_similar(building_1, building_2)
# print(returned_value)  
# print()

# print('==============Test Case 2=============')
# building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Yellow', 'Green']))
# building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
# print('Building 1: ', end=' ')
# printLinkedList(building_1)
# print('Building 2: ', end=' ')
# printLinkedList(building_2)
# returned_value = check_similar(building_1, building_2)
# print(returned_value)  # This should print 'Not Similar'
# print()

# print('==============Test Case 3=============')
# building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
# building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
# print('Building 1: ', end=' ')
# printLinkedList(building_1)
# print('Building 2: ', end=' ')
# printLinkedList(building_2)
# returned_value = check_similar(building_1, building_2)
# print(returned_value)  # This should print 'Not Similar'
# print()

# print('==============Test Case 4=============')
# building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
# building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
# print('Building 1: ', end=' ')
# printLinkedList(building_1)
# print('Building 2: ', end=' ')
# printLinkedList(building_2)
# returned_value = check_similar(building_1, building_2)
# print(returned_value)  # This should print 'Not Similar'
# print()

#TASK 2

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    
#     def createList(array):
#         print(array)


# def createList(array):
#     head =None
#     for i in array:
#         if head ==None:
#             node =Node(i)
#             head = node
#         else:
#             current =head
#             while current.next is not None:
#                 current =current.next
            
#             node =Node(i)
#             current.next =node
    
#     return head


# def printLinkedList(head):
#     current =head

#     while current is not None:
#         print(current.data,end="-->")
#         current=current.next
    
#     print(None)
# def remove_compartment(head,n):

#     current = head
#     count =0

#     while current is not None:
#         count+=1
#         current=current.next
    
#     pos = count-n;
#     if n > count:
#         return head
#     else:
#         if pos==0:
#             head = head.next
#             return head
                   
#         else:  
#             current = head
#             index=0
#             while current:
#                 if index  ==pos-1: #4
#                     current.next = current.next.next 
#                     break
#                 current =current.next
#                 index+=1
#             return head
                         
# import numpy as np
# print('==============Test Case 1=============')
# head = createList(np.array([10,15,34,41,56,72]))
# print('Original Compartment Sequence: ', end = ' ')
# printLinkedList(head)
# head = remove_compartment(head,2)
# print('Changed Compartment Sequence: ', end = ' ')
# printLinkedList(head) #This should print 10-->15-->34-->41-->72
# print()
# print('==============Test Case 2=============')
# head = createList(np.array([10,15,34,41,56,72]))
# print('Original Compartment Sequence: ', end = ' ')
# printLinkedList(head)
# head = remove_compartment(head,7)
# print('Changed Compartment Sequence: ', end = ' ')
# printLinkedList(head) #This should print 10-->15-->34-->41-->56-->72
# print()
# print('==============Test Case 3=============')
# head = createList(np.array([10,15,34,41,56,72]))
# print('Original Compartment Sequence: ', end = ' ')
# printLinkedList(head)
# head = remove_compartment(head,6)
# print('Changed Compartment Sequence: ', end = ' ')
# printLinkedList(head) #This should print 15-->34-->41-->56-->72
# print()

#TASK 3

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    
#     def createList(array):
#         print(array)


# def createList(array):
#     head =None
#     for i in array:
#         if head ==None:
#             node =Node(i)
#             head = node
#         else:
#             current =head
#             while current.next is not None:
#                 current =current.next
            
#             node =Node(i)
#             current.next =node
    
#     return head


# def printLinkedList(head):
#     current =head

#     while current is not None:
#         print(current.data,end="-->")
#         current=current.next
    
#     print(None)# class Node:
    
# def assemble_conga_line(conga_line):
#     current =conga_line
#     while current.next:
#         one =int(current.data)
#         two=int(current.next.data)
#         if one > two:
#             return ("False")
#         current =current.next
    
#     return ("True")


# import numpy as np
# print('==============Test Case 1=============')
# conga_line = createList(np.array([10,15,34,41,56,72]))
# print('Original Conga Line: ', end = ' ')
# printLinkedList(conga_line)
# returned_value = assemble_conga_line(conga_line)
# print(returned_value) #This should print True
# # unittest.output_test(returned_value, True)
# print()
# print('==============Test Case 2=============')
# conga_line = createList(np.array([10,15,44,41,56,72]))
# print('Original Conga Line: ', end = ' ')
# printLinkedList(conga_line)
# returned_value = assemble_conga_line(conga_line)
# print(returned_value) #This should print False
# # unittest.output_test(returned_value, False)
# print()

# TASK4

class Node:
  def __init__(self,elem,next = None):
    self.elem,self.next = elem,next

def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = Node(arr[i])
    tail.next = newNode
    tail = newNode
  return head

def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()


def word_Decoder(head):
    current =head

    index = 0

    dummy_head =None

    while current:
        if index %3 ==0 and index!=0 :
            if dummy_head ==None:
                node =Node(current.elem)
                dummy_head  =node
            else:
                node =Node(current.elem)
                node.next =dummy_head 
                dummy_head  =node
        current =current.next
        index+=1
    first_node = Node("None")
    first_node.next = dummy_head 
    dummy_head  =first_node
    return dummy_head 

#Driver Code
import numpy as np
print('==============Test Case 1=============')
head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))
print("Encoded Word:")
printLinkedList(head) 

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)   

print('==============Test Case 2=============')

head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))
print("Encoded Word:")
printLinkedList(head)

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→N

#TASK 5

# class Node:
#   def __init__(self,elem,next = None):
#     self.elem,self.next = elem,next

# def createList(arr):
#   head = Node(arr[0])
#   tail = head
#   for i in range(1,len(arr)):
#     newNode = Node(arr[i])
#     tail.next = newNode
#     tail = newNode
#   return head

# def printLinkedList(head):
#   temp = head
#   while temp != None:
#     if temp.next != None:
#       print(temp.elem, end = '-->')
#     else:
#       print(temp.elem)
#     temp = temp.next
#   print()



# def alternate_merge(head1, head2):
#     current1 = head1
#     current2 = head2

#     while current1 and current2:
#         next1 = current1.next
#         next2 = current2.next

#         current1.next = current2
#         current2.next = next1
        
#         current1 = next1
#         current2 = next2

#     return head1

# import numpy as np

# print('==============Test Case 1=============')
# head1 = createList(np.array([1,2,6,8,11]))
# head2 = createList(np.array([5,7,3,9,4]))

# print("Linked List 1:")
# printLinkedList(head1)
# print("Linked List 2:")
# printLinkedList(head2)

# head = alternate_merge(head1, head2)
# print("Merged Linked List:")
# printLinkedList(head)  

# print('==============Test Case 2=============')
# head1 = createList(np.array([5, 3, 2, -4]))
# head2 = createList(np.array([-4, -6, 1]))
# print("Linked List 1:")
# printLinkedList(head1)
# print("Linked List 2:")
# printLinkedList(head2)

# head = alternate_merge(head1, head2)
# print("Merged Linked List:")
# printLinkedList(head)   


# print('==============Test Case 3=============')
# head1 = createList(np.array([4, 2, -2, -4]))
# head2 = createList(np.array([8, 6, 5, -3]))

# print("Linked List 1:")
# printLinkedList(head1)
# print("Linked List 2:")
# printLinkedList(head2)

# head = alternate_merge(head1, head2)
# print("Merged Linked List:")
# printLinkedList(head)    #This should print   4-> 8 → 2-> 6 → -2 → 5 → -4 -> -3

#TASK6

#TASK6
# class Node:
#     def __init__(self, elem, next=None):
#         self.elem, self.next = elem, next


# def createList(arr):
#     head = Node(arr[0])
#     tail = head
#     for i in range(1, len(arr)):
#         newNode = Node(arr[i])
#         tail.next = newNode
#         tail = newNode
#     return head


# def printLinkedList(head):
#   temp = head
#   while temp != None:
#     if temp.next != None:
#       print(temp.elem, end = '-->')
#     else:
#       print(temp.elem)
#     temp = temp.next
#   print()


# def sum_dist(head, arr):     
#     sum =0
#     for i in arr:
#         current =head
#         index = 0
#         while current:
#             if i ==index:
#                 sum+=current.elem
#                 break
#             current =current.next
#             index+=1
            
#     return sum
       
# import numpy as np

# print('==============Test Case 1 =============')
# LL1 = createList(np.array([10, 16, -5, 9, 3, 4]))
# dist = np.array([2, 0, 5, 2, 8])
# returned_value = sum_dist(LL1, dist)
# print(f'Sum of Nodes: {returned_value}') 


