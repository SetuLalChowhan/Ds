import numpy as np

# #TASK 1
# def mergeLineup(pokemon_1, pokemon_2):
#     for i in range(len(pokemon_1)):
#         if pokemon_1[i] is None:
#             pokemon_1[i] = 0
#         if pokemon_2[i] is None:
#             pokemon_2[i] = 0
    
#     merged_lineup = np.zeros(len(pokemon_1), dtype=int)
#     for i in range(len(pokemon_1)):
#         merged_lineup[i] = pokemon_1[i] + pokemon_2[len(pokemon_2) - 1 - i]

#     return merged_lineup

# # Test cases
# print("/// Task 01: Merge Lineup ///")
# pokemon_1 = np.array([12, 3, 25, 1, None])
# pokemon_2 = np.array([5, -9, 3, None, None])
# returned_value = mergeLineup(pokemon_1, pokemon_2)
# print(f'Task 1: {returned_value}') 

# pokemon_1 = np.array([4, 5, -1, None, None])
# pokemon_2 = np.array([2, 27, 7, 12, None])
# returned_value = mergeLineup(pokemon_1, pokemon_2)
# print(f'Task 1: {returned_value}') 

# # TASK 2

# def discardCards(cards, t):
#     cards = np.array(cards)


#     result = np.zeros(len(cards), dtype=int)
    

#     result_index = 0

#     discard = True

#     for card in cards:
#         if card == t:
#             if discard:

#                 discard = False  
#             else:
#                 result[result_index] = card
#                 result_index += 1
#                 discard = True 
#         else:
#             result[result_index] = card
#             result_index += 1


#     return result
# cards1 = [1, 3, 7, 2, 5, 2, 2, 2, 0]
# print(discardCards(cards1, t=2)) 

# cards2 = [5, 5, 5, 0, 0]
# print(discardCards(cards2, t=5))  # Output: [5, 0, 0, 0, 0]

#task 3

# def decrypt_matrix(matrix):

#     rows = len(matrix)
#     cols = len(matrix[0])

#     # sumRow = np.zeros(rows,dtype=int)
    
#     # for i in range(rows):
#     #     sum=0
#     #     for j in matrix[i]:
#     #         sum+=j
#     #     sumRow[i]=sum
    
#     # print(sumRow)


#     newCol = np.zeros(cols,dtype=int)
    
#     for i in range(rows):
#         for j in range(cols):
#             newCol[j]+=matrix[i][j] //[1,0,0]
    
    
#     deff = np.array([0]*(cols-1),dtype=int)
   

#     for i in range(cols-1):
#         deff[i] =newCol[i+1]-newCol[i]
    

#     return deff
#   #To Do
# matrix=np.array([[1,3,1],
#                  [6,4,2],
#                  [5,1,7],
#                  [9,3,3],
#                  [8,5,4],
#                  ])

# returned_array=decrypt_matrix(matrix)
# print(returned_array)
# #This should print [-13, 1]


# def countZero(matrix):
#     rows = len(matrix)
#     cols =len(matrix[0])
#     count = 0 
#    #row
#     # for i in matrix:
#     #     for j in i:
#     #         if j==0:
#     #             count+=1
#                 #   break

#     #colume

#     for i in range(cols):
#         for j in range(rows):
#             if matrix[j][i] ==0:
#                 count+=1
#                 break
    
#     # return count

# matrix=np.array([[2,0,0],
#                  [0,4,2],
#                  [5,1,7],
#                  ])

# returned_array=countZero(matrix)
# print(returned_array)


