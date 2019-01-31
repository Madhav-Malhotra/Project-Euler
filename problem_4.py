#This program finds the largest palindrome that is the product of two 3-digit numbers.
#Madhav Malhotra

#This initialises necessary variables.
largestPalindrome = 0;
#This runs down possible 3-digit numbers
for num1 in range(999, 899, -1):
  #This runs down possible 3-digit numbers.
  for num2 in range(999, 899, -1):
    #This finds the products of the two 3-digit numbers.
    product = num1 * num2;
    #This checks if the product is a palindrome.
    productString = str(product);
    if productString[:] == productString[::-1]:
      #This checks if the current palindrome is larger than any other palindromes found.
      if product > largestPalindrome:
        #This saves the largest palindrome found
        largestPalindrome = product;
#This prints the largest palindrome found.
print(largestPalindrome);