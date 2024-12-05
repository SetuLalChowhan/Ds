# class Stack:
#     def __init__(self,max):
#         self.max=max
#         self.values = []
#         self.top=0
#     def push(self,x):
#         if(self.top ==self.max):
#            return print(f"Overflow")
#         self.values=self.values+[x]
#         self.top+=1

#     def pop(self):
#         if(self.top==0):
#             return print("Underflow")
#         self.top-=1
#         return self.values.pop()   

# s = Stack(5)
# s.push(5)
# s.push(6)
# s.push(2)
# s.push(1)
# s.push(12)
# s.pop()
# print(s.values)  
 
# class Node:
#     def __init__(self, elem=None, next=None):
#         self.elem = elem
#         self.next = next


# class Stack:
#     def __init__(self):
#         self.__top = None

#     def push(self, elem):
#         nn = Node(elem, self.__top)
#         self.__top = nn

#     def pop(self):
#         if self.__top is None:
#             return None
#         e = self.__top
#         self.__top = self.__top.next
#         return e.elem

#     def peek(self):
#         if self.__top is None:
#             return None
#         return self.__top.elem

#     def isEmpty(self):
#         return self.__top is None


# def print_stack(st):
#     if st.isEmpty():
#         return
#     p = st.pop()
#     print('|', p, end=' ')
#     if p < 10:
#         print(' |')
#     else:
#         print('|')
#     print_stack(st)
#     st.push(p)

# # stack =Stack()
# stack.push(5)
# stack.push(6)
# stack.push(10)
# stack.pop()

# print(stack.peek())
# print_stack(stack)

# def diamond_count(stack, string):
#     diamond_count = 0
#     for char in string:
#         if char == '<':
#             stack.push(char) 
#         elif char == '>':
#             if not stack.isEmpty() and stack.peek() == '<':
#                 stack.pop()  
#                 diamond_count += 1  
#     return diamond_count


# # Test Cases
# print('Test 01')
# stack = Stack()
# string = '<..><.<..>> '
# returned_value = diamond_count(stack, string)
# print(f'Number of Diamonds: {returned_value}')  # Should print 3
# print('-----------------------------------------')

# print('Test 02')
# stack = Stack()
# string = '<<<..<......<<<<....>'
# returned_value = diamond_count(stack, string)
# print(f'Number of Diamonds: {returned_value}')  # Should print 1
# print('-----------------------------------------')

# print('Test 03')
# stack = Stack()
# string = '>>><...<<..>>...>...>>>'
# returned_value = diamond_count(stack, string)
# print(f'Number of Diamonds: {returned_value}')  # Should print 3
# print('-----------------------------------------')


# def remove_block(stack, n):
#     temp_stack = Stack()

#     if stack.isEmpty() or n <= 0:
#         print("Invalid operation: Stack is empty or invalid position")
#         return

#     count = 0
#     while not stack.isEmpty() and count < n - 1:
#         temp_stack.push(stack.pop())
#         count += 1

#     if not stack.isEmpty():
#         stack.pop()
#     else:
#         print("Invalid operation: n is larger than the size of the stack")
#         while not temp_stack.isEmpty():
#             stack.push(temp_stack.pop())
#         return

#     while not temp_stack.isEmpty():
#         stack.push(temp_stack.pop())


# print('Test 01')
# st = Stack()
# st.push(4)
# st.push(19)
# st.push(23)
# st.push(17)
# st.push(5)
# print('Stack:')
# print_stack(st)
# print('------')
# remove_block(st, 2)
# print('After Removal:')
# print_stack(st)
# print('------')

# print()
# print('======================================')
# print()

# print('Test 02')
# st = Stack()
# st.push(73)
# st.push(85)
# st.push(15)
# st.push(41)
# print('Stack:')
# print_stack(st)
# print('------')
# remove_block(st, 3)
# print('After Removal:')
# print_stack(st)
# print('------')

# print()
# print('======================================')
# print()
# hi this is no