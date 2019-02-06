#This program finds the difference between the square of the sum of the first 100 numbers and the sum of the squares of the first 100 numbers.
#Madhav Malhotra

#This stores the sum of the numbers
base = 0;
#This stores the sum of the numbers' squares
sumSquares = 0;
#Go from 1 to 100.
for num in range(1, 101):
  #Add to total base
  base += num;
  #Square each number
  numSquare = num**2;
  #Add to total square
  sumSquares += numSquare;
#Square total base 
base = base**2;
#Subtract total square
print(base - sumSquares);