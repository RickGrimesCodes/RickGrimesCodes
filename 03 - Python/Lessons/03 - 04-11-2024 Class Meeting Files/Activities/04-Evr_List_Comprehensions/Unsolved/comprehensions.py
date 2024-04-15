# @TODO: Your code here

first4Letters = "ABCD"
#letter = []
#for letter in first4Letters:
#   letters.append(letter)




# we can condense the lines 5-7 down to make the list using a comprehension 
   # letters = -> list that we make
   # first 'letter' -> value that is appended to the list
   # 'for letter in first4Letters' -> loop that is executed
letters = [letter for letter in first4Letters]
print(letters)

# in this go around, we want to do lowercase letters

lowerCaseLetters = [letter.lower() for letter in first4Letters]
print(lowerCaseLetters)

# given this list of numbers,
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# if we want  to make a list of odd numbers, we could do the following:
oddNumbers = []
for number in numbers:
    if number % 2 != 0:
        oddNumbers.append(number)
oddNumbers = [number for number in numbers if number % 2 != 0]
print(oddNumbers)