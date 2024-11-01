# import numpy as np  #nd array create

#create array
# l1=[10,20,30,40,11,1,2,3,4]
# l2=[[2,3,4],[22,21,22],[1,2,3],[31,32,33]]
# array1 = np.array(l1)
# array2 = np.array(l2,dtype=int)
# array3 = np.arange(1,8)
# array4 = np.arange(11,17).reshape((3,2))
# array5 =np.zeros(4,dtype=int)
# array6 =np.ones(4,dtype=int)
# print(array6)

#attribute of Numpy
# 1.ndim
# 2.shape
# 3.size
# 4.dtype
# 5.itemsize

# print(array2.ndim)

# print(array2.shape)

# print(array1.size)

# print(array1.dtype)
# print(array1.itemsize)

#indexing in Numpy Array

# print(array1[3])
# print(array2[1,2])
# print(array2[0,:]) row and colume
# print(array2[:,1])

#slicing
# 1d [start,stop,step]
# print(array1[1:3]) 
# print(array1[1:6:2])\
# print(array1[-1:-3:-1])
# print(array1[::2])
# print(array1[::-1])
# 2d [[rowstart:rowend],[columestart:columeend]]
# print(array2)
# print(array2[1,])
# print(array2[:,1])
# print(array2[1:3,1:3])
# print(array2[1:3,])
# print(array2[:,1:3])
# print(array2[1:3,1])

#arithmatic operations on Numpy Arrays
# 1.Addition(+)
# 2.Subtraction(-)
# 3.Multiplication(*)
# 4.Matrix Multipliccation(@)
# 5.Division(/)
# 6.Floor Division(//)
# 7.Exponentiation(**)
# 8.Transpose

# x = np.array([[1,2],[3,4]])
# y = np.array([[11,12],[13,14]])

# z= x+y
# z= x-y
# z=x*y
# z =x@y
# z=y/x
# z=y//x
# z=y**x
# z=y%x
# print(z)
# print(x.transpose())

# sorting 2d array

# x =np.array([[12,11,15],[21,25,20],[18,27,16]])

# y= np.sort(x)
# y= np.sort(x,axis=1)
# y= np.sort(x,axis=0)
# y = x.argsort(x,axis=1)
# y = x.argsort(x,axis=0)
# print(y)
