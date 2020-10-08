import random

'''
0 = empty seat
1 = randomly assigned economy seat
2 = specifically assigned premium seat
'''

economy_seats = 0
premium_seats = 0
num_rows = int(input("How many rows are in the plane? "))
num_columns = int(input("How many columns are in the plane? "))
seats = num_rows*num_columns

# making a 2D array of the plane of rows, cols
def make_a_plane(rows, cols):
  plane = [[0 for x in range(rows)] for y in range(cols)]
  return plane

def show_plane(plane):
  for i in plane:
    print(i)

# this function changes the value of a seat at x,y:
def assign_seat(plane,seat_row,seat_column,value): 
  plane[seat_row][seat_column] = value

def choose_seat(plane):
  global seats
  global premium_seats
  show_plane(plane)
  seat_row = int(input("What row would you like? "))
  seat_column = int(input("What column would you like? "))
  if plane[seat_row][seat_column] == 2:
    print("Sorry, that seat is taken")
    choose_seat(plane)
  elif plane[seat_row][seat_column] == 0:
    print("That seat is available!")
    assign_seat(plane,seat_row,seat_column,2)
    seats -= 1
    premium_seats += 1
    print('seats left = ',seats)
    print('premium seats = ',premium_seats)
    print('economy seats = ',economy_seats)
  elif plane[seat_row][seat_column] == 1:
    print("That seat is available!")
    assign_seat(plane,seat_row,seat_column,2)
    economy(plane)
    premium_seats += 1
    seats -= 1
    print('seats left = ',seats)
    print('premium seats = ',premium_seats)
    print('economy seats = ',economy_seats)

def economy(plane):
  seat_row = random.randint(0, num_rows-1)
  seat_column = random.randint(0,num_columns-1)
  if plane[seat_row][seat_column] !=0:
    economy(plane)
  else: 
    assign_seat(plane,seat_row,seat_column,1)

#~~~~~Main~~~~~#
plane = make_a_plane(num_rows,num_columns)

while seats !=0:
  customer = int(input("What kind of customer are you? (1 for economy, 2 for premium) "))
  if customer == 1:
    economy(plane)
    economy_seats += 1
    seats -= 1
    print('seats left = ',seats)
    print('premium seats = ',premium_seats)
    print('economy seats = ',economy_seats)
  if customer == 2:
    choose_seat(plane)
  print("Here is your seat:")
  show_plane(plane)
  print('\n')

print("Plane is full!")