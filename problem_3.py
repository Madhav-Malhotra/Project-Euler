#This program finds the greatest prime factor of 600851475143.
#Madhav Malhotra

#This initialises necessary variables.
numInput = 600851475143;
#This holds the factors found.
factors = [];
#This loop runs until all factors are found.
while not(numInput == 1):
  #This finds factors
  for num in range(2, numInput):
    if numInput % num == 0:
      numInput //= num;
      #This saves any factors found
      factors.append(num);
      #This breaks from the loop once all factors are found.
      if numInput == 1:
        break;
#This holds prime factors out of the factors found.
primeFactors = [];
#This tests if the factors are prime.
for factor in factors:
  prime = True;
  for divisibilityTest in factors:
    if divisibilityTest == factor:
      continue;
    else:
      if factor % divisibilityTest == 0:
        prime = False;
  #If the current factor is prime, it is saved.
  if prime == True:
    primeFactors.append(factor);
#This initialises the greatest prime factor.
greatestPrimeFactor = 1;
#This looks for the greatest factor in the prime factors.
for num in primeFactors:
  if num > greatestPrimeFactor:
    greatestPrimeFactor = num;
#This prints the greatest prime factor.
print(greatestPrimeFactor);