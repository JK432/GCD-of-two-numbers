#The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly divided into both of them. Euclid’s algorithm can be used to find the greatest common divisor(GCD) of two positive integers. You can use this algorithm in the following manner. a. Compare the remainder of dividing the largest number by the smallest number. b. Replace the largest number with the smallest number and the smaller number with the remainder c. Repeat this process until the smaller number is zero The larger number at this point is the GCD of A and B. Write a program that lets the user to enter two integers and then prints each step in the process of using the Euclid’s algorithm to find their GCD

x=int(input())
y=int(input())
if x>y:
  small=y
  large=x
else:
  small=x
  large=y

i=0
while small>0:
  rem=large%small
  if rem>small:
    large=rem
    small=small
  elif rem==0:
    print(small)
    break
  else:
    small=rem
    large=small