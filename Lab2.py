
class Node:
    def __init__(self,data):
        self.color = data
        self.next = None
    
    def createList(array):
        print(array)


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

print('==============Test Case 1=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end=' ')
printLinkedList(building_1)
print('Building 2: ', end=' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value)  # This should print 'Similar'
print()

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
