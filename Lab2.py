#TASK 1
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
#             delPos=0
#             while current:
#                 if delPos  ==pos-1:
#                     current.next = current.next.next 
#                     break
#                 current =current.next
#                 delPos+=1
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

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def createList(array):
        print(array)


def createList(array):
    head =None
    for i in array:
        if head ==None:
            node =Node(i)
            head = node
        else:
            current =head
            while current.next is not None:
                current =current.next
            
            node =Node(i)
            current.next =node
    
    return head


def printLinkedList(head):
    current =head

    while current is not None:
        print(current.data,end="-->")
        current=current.next
    
    print(None)# class Node:
    
def assemble_conga_line(conga_line):
    current =conga_line
    while current.next:
        one =int(current.data)
        two=int(current.next.data)
        if one > two:
            print("hi")
            return ("False")
        current =current.next
    
    return ("True")


import numpy as np
print('==============Test Case 1=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print True
# unittest.output_test(returned_value, True)
print()
print('==============Test Case 2=============')
conga_line = createList(np.array([10,15,44,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print False
# unittest.output_test(returned_value, False)
print()