"""Whip up a python apparatus for randomly populating a state with partisan voters:
State is a 6x3 grid of cells. 1. What is your state's name? 2. Each cell is inhabited entirely by citizens who vote '1' XOR citizens who vote '0'.
Your program should be able to: 
Randomly populate each cell with a 1 or 0. Display a generated configuration.
Divide your state into 6 "districts":
A district is a list of coordinate pairs, where each pair represents a member cell.
A district must be comprised of adjacent cells.
Primary goal: ensure each cell is in a district.
Secondary goal: balance district sizes. """
import random

name_of_State = input("What is the name of the State? ") #Ask for the name of your state

# Make a grid of 6 by 3 cells.
rows, cols = (6,3)
Districts = []

# Make 2D array to generate either 1(s) or 0(s) wthin specific district
for i in range (rows):
  ROW = []
  for j in range (cols):
    ROW.append(random.randint(0,1))
  Districts.append(ROW)

# Show voting result within each district
print("\nIn " + str(name_of_State) + ", this is how your districts voted: \n")
for i in range (rows):
  print("District " + str(i+1) + ": " + " ")
  print (Districts[i])
  print("\n")