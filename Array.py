# import ctypes
# class MyList:
#     def __init__(self):
#         self.size =1
#         self.n=0
#         self.A= self.__make_array(self.size)
#     def __make_array(self,capacity):
#         #ctype
#         return (capacity*ctypes.py_object)()
#     def __len__(self):
#         return self.n
#     def __str__(self):
#         result =''
#         for i in range(self.n):
#             result =result + str(self.A[i])+"," 
#         return "["+result[:-1]+"]"
#     def append(self,item):
#         if self.size == self.n:
#             #call
#             self.__resize(self.size*2)
#         self.A[self.n]=item
#         self.n+=1
#     def insert(self,pos,item):
#         if self.size ==self.n:
#             self.__resize(2*self.size)
#         for i in range(self.n-1,pos-1,-1):
#             self.A[i+1] =self.A[i]    
#         self.A[pos] =item
#         self.n=self.n+1
#     def delete(self,pos):
#         for i in range(pos,self.n-1):
#             self.A[i]=self.A[i+1]
#         self.n=self.n-1
#     def find(self,item):
#         for i in range(self.n):
#             if self.A[i] == item:
#                 return i
#         return "Value Error"  
#     def pop(self):
#         if self.n==0:
#             return "empty list"
#         self.n-=1
#         print(self.A[self.n-1])
#     def clear(self):
#         self.n=0
#         self.size=1
#     def __resize(self,new_capacity):
#         #create new array with double capacity
#        B = self.__make_array(new_capacity)
#        self.size =new_capacity
#        #copy the content of A to B
#        for i in range(self.n):
#            B[i] =self.A[i]
#        #reassign
#        self.A=B

# L=MyList()
# L.append(12)
# L.append(14)
# L.append(17)
# L.append(11)
# L.clear()
# L.pop()
# print(L)
# L.delete(1)
# print(L)
# L.insert(2,20)
# print(L)





