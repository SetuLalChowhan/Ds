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


#TASK 3

# def decrypt_matrix(matrix):

#     rows = len(matrix)
    
#     cols = len(matrix[0])

#     newCol = np.zeros(cols,dtype=int)
    
#     for i in range(rows):
#         for j in range(cols):
#             newCol[j]+=matrix[i][j] 
    
    
#     deff = np.zeros(cols-1,dtype=int)
   

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
#TASK 4

# def print_matrix(matrix):
#     print(matrix)

# def walk_zigzag(floor):
#     rows = len(floor)
#     cols =len(floor[0])
#     for col in range(cols):
#         if col % 2 == 0:  
#             for row in range(rows):
#                 if(row%2==0):
#                     print(floor[row][col], end=" ")
#         else:  
#             for row in range(rows):
#                 reverse_row = rows - 1 - row
#                 if reverse_row % 2 != 0:
#                     print(floor[reverse_row][col], end=" ")
#         print()  

# # Test case 1
# floor = np.array([['3', '8', '4', '6', '1'],
#                   ['7', '2', '1', '9', '3'],
#                   ['9', '0', '7', '5', '8'],
#                   ['2', '1', '3', '4', '0'],
#                   ['1', '4', '2', '8', '6']])

# print_matrix(floor)
# print('Walking Sequence:')
# walk_zigzag(floor)

# print('################')

# # Test case 2
# floor = np.array([['3', '8', '4', '6', '1'],
#                   ['7', '2', '1', '9', '3'],
#                   ['9', '0', '7', '5', '8'],
#                   ['2', '1', '3', '4', '0']])

# print_matrix(floor)
# print('Walking Sequence:')
# walk_zigzag(floor)

#TAKS 5

# def print_matrix(matrix):
#     print(matrix)
   

# def row_rotation(exam_week, seat_status):
#     rows = len(seat_status)
#     cols = len(seat_status[0])
#     rotated_seat_status = [[None for _ in range(cols)] for _ in range(rows)]  

#     for i in range(rows):
#         for j in range(cols):
#             rotated_seat_status[i][j] = seat_status[i][j]
#     shift = (exam_week - 1) % rows  


#     for _ in range(shift):

#         last_row = rotated_seat_status[rows - 1]  
#         for i in range(rows - 1, 0, -1):
#             rotated_seat_status[i] = rotated_seat_status[i - 1] 
#         rotated_seat_status[0] = last_row  

#     print("Seat status after rotation:")
#     print_matrix(rotated_seat_status)

#     for i in range(rows):
#         if 'AA' in rotated_seat_status[i]:
#             return i + 1 


# seat_status = [
#     ['A', 'B', 'C', 'D', 'E'],
#     ['F', 'G', 'H', 'I', 'J'],
#     ['K', 'L', 'M', 'N', 'O'],
#     ['P', 'Q', 'R', 'S', 'T'],
#     ['U', 'V', 'W', 'X', 'Y'],
#     ['Z', 'AA', 'BB', 'CC', 'DD']
# ]

# exam_week = 3
# print("Original seat status:")
# print_matrix(seat_status)
# print()

# row_number = row_rotation(exam_week, seat_status)
# print(f'Your friend AA will be on row {row_number}')



#TASK 6

def print_matrix(matrix):
    print(matrix)
def compress_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    compressed_rows = rows // 2
    compressed_cols = cols // 2
    compressed_mat = np.zeros((compressed_rows, compressed_cols), dtype=int)
    for i in range(0, rows, 2):
        for j in range(0, cols, 2):
           
            block_sum = (mat[i][j] + mat[i+1][j] +
                         mat[i][j+1] + mat[i+1][j+1])
           
            compressed_mat[i//2][j//2] = block_sum
    
    return compressed_mat


matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
print("...............")
returned_array=compress_matrix(matrix)
print_matrix(returned_array)


# TASK7

# def print_matrix(matrix):
#     print(matrix)
# def play_game(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     total_points = 0

#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] % 50 == 0 and matrix[i][j] != 0:  

#                 points = 0
#                 if i > 0 and matrix[i - 1][j] == 2:  
#                     points += 2
#                 if i < rows - 1 and matrix[i + 1][j] == 2:  
#                     points += 2
#                 if j > 0 and matrix[i][j - 1] == 2:  
#                     points += 2
#                 if j < cols - 1 and matrix[i][j + 1] == 2:  
#                     points += 2
              
#                 total_points += points

#     print("Points Gained:", total_points)
#     if total_points >= 10:
#         print("Your team has survived the game.")
#     else:
#         print("Your team is out.")
# arena=np.array([[0,2,2,0],
#                 [50,1,2,0],
#                 [2,2,2,0],
#                 [1,100,2,0]
#                 ])
# print_matrix(arena)
# play_game(arena)
# print(".....................")
# arena=np.array([[0,2,2,0,2],
#                 [1,50,2,1,100],
#                 [2,2,2,0,2],
#                 [0,200,2,0,0]
#                 ])
# print_matrix(arena)
# play_game(arena)


