import sys
s = 100
for arg in sys.argv[1:]:
    number = int(arg)
    s += number
even_Sum = 0
odd_Sum = 0
for num in range(1, s+1):
    if (num % 2 == 0):
# Addition of even numbers
        even_Sum = even_Sum + num
    else:
# Addition of odd numbers
        odd_Sum = odd_Sum + num
print("The sum of Even numbers 1 to {0} = {1}".format(num, even_Sum))
print("The sum of Even numbers 1 to {0} = {1}".format(num, odd_Sum))
# Substraction of even_sum from odd_sum
sub = even_Sum - odd_Sum
print('Difference is: ', sub)
