#This program finds the sum of all the multiples of 5 and 3 that are less than 1000.
#Madhav Malhotra

#This initialises the sum variable
sum = 0;
#This initialises a list to hold all the multiples
multiples = [];
#This goes from 3 to 999
for num in range (3, 1000):
  #This checks if the current number is divisible
  #by 3 or 5
  if num % 3 == 0 or num % 5 == 0:
    #This checks if the multiple has already
    #been found
    if num not in multiples:
      #If the multiple is new, it is saved.
      multiples.append(num);
#This goes through all the multiples found
for num in multiples:
  #This adds each multiple to the sum.
  sum += num;
#This returns the final sum
print(sum);
