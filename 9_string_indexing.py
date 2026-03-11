# indexing = accessing elements of a sequence using [] (indexing operators)
#            [start : end : stop]
#            start: It includes mentioned the char or int
#            end: It excludes the mentioned char or int

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # Prints first element
print(credit_number[-1]) # Prints from the reverse when used (-)ve, so the print output would be 6

print(credit_number[0:4]) # Print from 1 till 4 cause [0->1  1->1  2->2   2->3] = the count is 4 but reached only 3rd place element, it won't include the 4th term that is '-' as it excludes it
print(credit_number[:4]) # Assumes that 0 is the starting position

print(credit_number[5:9]) # Prints 5678 as the 5th element -> 5 and it won't include the 9th element that is -> -
print(credit_number[5:]) # Assumes that we require the rest of the element from the given position till end

print(credit_number[::2]) # Assuming we require all the elements from start to end but jumping 2 places, output: 13-6891-46
print(credit_number[::3]) # Assuming we require all the elements from start to end but jumping 2 places, output: 146-136

print(credit_number[::-1]) # Wants to print the element in reverse

# If want the last 4 digits of the credit card:
print(f"The last four digit of the credit card: {credit_number[-4:]}")