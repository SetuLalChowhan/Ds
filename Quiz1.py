import numpy as np

#TASK 1
def mergeLineup(pokemon_1, pokemon_2):
    for i in range(len(pokemon_1)):
        if pokemon_1[i] is None:
            pokemon_1[i] = 0
        if pokemon_2[i] is None:
            pokemon_2[i] = 0
    
    merged_lineup = np.zeros(len(pokemon_1), dtype=int)
    for i in range(len(pokemon_1)):
        merged_lineup[i] = pokemon_1[i] + pokemon_2[len(pokemon_2) - 1 - i]

    return merged_lineup

# Test cases
print("/// Task 01: Merge Lineup ///")
pokemon_1 = np.array([12, 3, 25, 1, None])
pokemon_2 = np.array([5, -9, 3, None, None])
returned_value = mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') 

pokemon_1 = np.array([4, 5, -1, None, None])
pokemon_2 = np.array([2, 27, 7, 12, None])
returned_value = mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') 

#TASK 2

# def discardCards(cards, t):
#     # Convert input list to a NumPy array
#     cards = np.array(cards)

#     # Initialize a NumPy array for results with the same size, filled with zeros
#     result = np.zeros(len(cards), dtype=int)
    
#     # Index to keep track of where to place the next valid card
#     result_index = 0
    
#     # Flag to determine whether to discard or keep the current occurrence of t
#     discard = True

#     # Iterate through the original cards
#     for card in cards:
#         if card == t:
#             if discard:
#                 # Discard the card (do nothing)
#                 discard = False  # Next occurrence will be kept
#             else:
#                 # Keep the card by adding it to the result
#                 result[result_index] = card
#                 result_index += 1
#                 discard = True  # Next occurrence will be discarded
#         else:
#             # If the card is not t, keep it in the result
#             result[result_index] = card
#             result_index += 1

#     # Return the result array with only the valid cards and zeros in unused positions
#     return result

# # Sample Input / Driver Code
# cards1 = [1, 3, 7, 2, 5, 2, 2, 2, 0]
# print(discardCards(cards1, t=2))  # Output: [1, 3, 7, 5, 2, 2, 0, 0, 0]

# cards2 = [5, 5, 5, 0, 0]
# print(discardCards(cards2, t=5))  # Output: [5, 0, 0, 0, 0]


# def decrypt_matrix(matrix):
#     # Convert the input list to a NumPy array for easier manipulation
#     np_matrix = np.array(matrix)
    
#     # Calculate the sum of each column
#     column_sums = np.sum(np_matrix, axis=0)
    
#     # Calculate the differences between subsequent column sums
#     differences = np.diff(column_sums)
    
#     return differences.tolist()  # Convert the result to a list before returning

# # Sample Input
# matrix = [
#     [1, 3, 1],
#     [6, 4, 2],
#     [5, 1, 7],
#     [9, 3, 3],
#     [8, 5, 4]
# ]

# # Function Call
# result = decrypt_matrix(matrix)
# print(result)  # Output: [-13, 1]

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
#             newCol[j]+=matrix[i][j]
    
    
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

