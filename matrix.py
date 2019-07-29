from random import randint

import numpy as np
zeors_array = np.zeros( [10,10], dtype=np.int32 )

row = randint(0, 9)
col = randint(0, 9)
print 'row:', row
print 'col:', col

p_vec = row * 10 + col #place_vector the first index is 0 so we need to write +1

zeors_array = np.insert( zeors_array, p_vec, 1)
zeors_array = np.delete( zeors_array, p_vec+1)
zeors_array = np.resize( zeors_array, (10,10))
print zeors_array

row_from_p = 10 - (row + 1)
r_col_from_p = 10 - (col + 1) #because in p_vec we wrote col+1
up_row_from_place = row
l_col_from_p = col
print 'down:', row_from_p #row_from_place
print 'right:', r_col_from_p #right_colum_from_place
print 'up:', up_row_from_place
print 'left:', l_col_from_p #left_colum_from_place

zeors_array = np.insert( zeors_array, 78, 2)
zeors_array = np.delete( zeors_array, 79)
zeors_array = np.insert( zeors_array, 21, 2)
zeors_array = np.delete( zeors_array, 22)
zeors_array = np.insert( zeors_array, 53, 2)
zeors_array = np.delete( zeors_array, 54)
zeors_array = np.insert( zeors_array, 2, 2)
zeors_array = np.delete( zeors_array, 3)
zeors_array = np.resize( zeors_array, (10,10))
print zeors_array

try1 = 0
while try1 < 40:
  word = raw_input("where to: ")
  if word == 'down':
    row += 1
    p_vec = row * 10 + col
    if row >= 10:
      print 'deadend... try again!'
      row -= 1
    elif p_vec == 78 or p_vec == 21 or p_vec == 53 or p_vec == 2:
      print 'sorry, there is an obstacle there.'
      print 'try again!'
      row -= 1
    else:
      print 'you\'r agent is in', p_vec
      zeors_array = np.insert( zeors_array, (row - 1) * 10 + col ,0)
      zeors_array = np.delete( zeors_array, ((row - 1) * 10 + col)+1)
      zeors_array = np.insert( zeors_array, p_vec, 1)
      p_vec += 1
      zeors_array = np.delete( zeors_array, p_vec)
      zeors_array = np.resize( zeors_array, (10,10))
      print zeors_array
      print
  elif word == 'up':
    row -= 1
    p_vec = row * 10 + col
    if row < 0:
      print 'deadend... try again!'
      row += 1
    elif p_vec == 78 or p_vec == 21 or p_vec == 53 or p_vec == 2:
      print 'sorry, there is an obstacle there.'
      print 'try again!'
      row += 1
    else:
      print 'you\'r agent is in', p_vec
      zeors_array = np.insert( zeors_array, (row + 1) * 10 + col ,0)
      zeors_array = np.delete( zeors_array, ((row + 1) * 10 + col) + 1)
      zeors_array = np.insert( zeors_array, p_vec, 1)
      p_vec = p_vec+1
      zeors_array = np.delete( zeors_array, p_vec)
      zeors_array = np.resize( zeors_array, (10,10))
      print zeors_array
      print
  elif word == 'left':
    col -= 1
    p_vec = row * 10 + col
    if col < 0:
      print 'deadend... try again!'
      col += 1
    elif p_vec == 78 or p_vec == 21 or p_vec == 53 or p_vec == 2:
      print 'sorry, there is an obstacle there.'
      print 'try again!'
      col += 1
    else:
      print 'you\'r agent is in', p_vec
      zeors_array = np.insert( zeors_array, p_vec + 1 ,0)
      zeors_array = np.delete( zeors_array, p_vec + 2)
      zeors_array = np.insert( zeors_array, p_vec, 1)
      p_vec = p_vec + 1
      zeors_array = np.delete( zeors_array, p_vec)
      zeors_array = np.resize( zeors_array, (10,10))
      print zeors_array
      print
  elif word == 'right':
    col += 1
    p_vec = row * 10 + col
    if col > 9:
      print 'deadend... try again!'
      col -= 1
    elif p_vec == 78 or p_vec == 21 or p_vec == 53 or p_vec == 2:
      print 'sorry, there is an obstacle there.'
      print 'try again!'
      col -= 1
    else:
      print 'you\'r agent is in', p_vec
      zeors_array = np.insert( zeors_array, p_vec - 1 ,0)
      zeors_array = np.delete( zeors_array, p_vec)
      zeors_array = np.insert( zeors_array, p_vec, 1)
      p_vec += 1
      zeors_array = np.delete( zeors_array, p_vec)
      zeors_array = np.resize( zeors_array, (10,10))
      print zeors_array
      print
  else:
    print 'where do you want me to go?'
    print 'try again!'
  try1 += 1
