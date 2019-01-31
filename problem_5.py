#This finds the least common multiple of all the numbers from 1 to 20. 
#Madhav Malhotra

def greatestCommonDivisor(num1, num2):
  '''
  This finds the greatest common denominator (GCD) of two numbers
  Input: Two positive integers
  Output: Positive integer
  '''
  #This organsises the first number as the bigger of the two.
  if num2 > num1:
    temp = num1;
    num1 = num2;
    num2 = temp;
  #This uses the Euclidean algorithm to find the GCD.
  while not(num2 == 0):
    remainder = num1 % num2;
    num1 = num2;
    num2 = remainder;
  #This returns the GCD.
  return num1;

def leastCommonMultiple(num1, num2):
  '''
  This finds the least common multiple (LCM) of two numbers
  Input: Two positive integers
  Output: Positive integer
  '''
  #This finds the GCD.
  gcd = greatestCommonDivisor(num1, num2);
  #This returns the LCM found by GCD reduction
  return (num1 // gcd) * num2;

#This an optimised list of numbers to find the least common multiple of all numbers from 1 to 20.
divisibilityCheck = [20, 18, 16, 14, 11, 13, 17, 19];
#This initialises necessary variables.
previousLCM = 1;
#This finds the least common multiple of all numbers provided.
for num in divisibilityCheck:
  previousLCM = leastCommonMultiple(num, previousLCM);
#This prints the least common multiple of all numbers from 1 to 20.
print(previousLCM);