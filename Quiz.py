# Quiz1
# import numpy as np
# def countZero(matrix):
#     rows = len(matrix)
#     cols =len(matrix[0])
#     count = 0 
# #    row
#     for i in matrix:
#         for j in i:
#             if j==0:
#                 count+=1
#                 break

#     #colume

#     for i in range(cols):
#         for j in range(rows):
#             if matrix[j][i] ==0:
#                 count+=1
#                 break
    
#     return count

# matrix=np.array([[2,0,1],
#                  [0,4,2],
#                  [5,1,7],
#                  ])

# returned_array=countZero(matrix)
# print(returned_array)

# Quiz 2

class Node:
    def __init__(self, elem, next=None):
        self.elem, self.next = elem, next


def createList(arr):
    head = Node(arr[0])
    tail = head
    for i in range(1, len(arr)):
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


def swap(head):  
    current =head

    index = 1
    count =0
    while current:
        current=current.next
        count+=1
    
    start =2
    end =count-1
    current =head
    first_node =None
    last_node=None
    while current:
        if index ==2 :
            first_node = current.elem
        
        if index ==end:
            last_node = current.elem
        current =current.next
        index+=1  
    current =head
    while current:
        if first_node == current.elem:
            current.elem =last_node
        
        elif last_node == current.elem:
            current.elem =first_node   
        current =current.next
    return head
import numpy as np

print('==============Test Case 1 =============')
LL1 = createList(np.array([10, 16, -5, 9, 3, 4]))
printLinkedList(LL1)
returned_value = swap(LL1)
printLinkedList(returned_value)