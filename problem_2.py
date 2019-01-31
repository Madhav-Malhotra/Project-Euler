#This program finds the sum of all the even Fibonacci terms that are less than 4 000 000.
#Madhav Malhotra

#This holds any even fibonacci terms found.
evenFib = [];
#This initialises the variables needed.
currentNum = 1;
previousNum = 0;
newNum = 0;
sum = 0;
#This keeps calculating Fibonacci terms while they are less than 4 000 000.
while newNum < 4000000:
  #This calculates Fibonacci terms
  newNum = currentNum + previousNum;
  previousNum = currentNum;
  currentNum = newNum;
  #This checks if the current term is even and less than 4 000 000.
  if currentNum % 2 == 0 and newNum <4000000:
    #This saves any terms that meet the constraints.
    evenFib.append(currentNum);
#This adds together all the even Fibonacci terms found that are less than 4 000 000.
for num in evenFib:
  sum += num;
#This prints the sum
print(sum);