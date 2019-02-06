#This finds the 10 001st prime number using a prime number generator.
#Madhav Malhotra

def primeGenerator(limit):
  '''
  This function generates primes less than the given limit using the sieve of Eratosthenes. It returns all the primes found in a list. 
  Input: Positive integer
  Output: List  
  '''
  #This initially assumes all numbers are prime.
  testList = [True] * (limit+1);
  #This goes through the possible primes within the limit.
  for num in range(2, int(limit**(1/2) + 1)):
    #This checks if the current number is prime. 
    if testList[num] == True:
      #This marks all multiples of the current number as composite.
      for multiple in range(num**2, limit, num):
        testList[multiple] = False;
  #This stores the primes found
  primes = [];
  #This adds any primes found to the list.
  for prime in range(2, limit):
    if testList[prime] == True:
      primes.append(prime);
  #This returns the primes found.
  return primes;

primes = primeGenerator(150000);
print(primes[10000]);