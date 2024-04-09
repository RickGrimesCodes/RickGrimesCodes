"""
    single alternative decisions - if statements
    VB:
    If condition Then
        statements
    End If
    python:
    if condition:
        statements
"""
# get an input
number = int(input("Enter a number: "))
# check to see if the number is even
if number % 2 == 0:
    print("Your number is even")
# display the number entered
print(f"You entered the number: {number}")
---------------------------------------------------------
"""
    single alternative decisions - if statements
    VB:
    If condition Then
        statements
    End If
    python:
    if condition:
        statements
    dual alternative decisions - if / else statements
    VB:
    If condition Then
        statements
    Else
        statements
    End If
    python:
    if condition:
        statements
    else:
        statements
"""
# get an input
number = int(input("Enter a number: "))
# check to see if the number is even or odd
if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")
# display the number entered
print(f"You entered the number: {number}")
-------------------------------------
"""
    single alternative decisions - if statements
    VB:
    If condition Then
        statements
    End If
    python:
    if condition:
        statements
    dual alternative decisions - if / else statements
    VB:
    If condition Then
        statements
    Else
        statements
    End If
    python:
    if condition:
        statements
    else:
        statements
    multiple alternative decisions - if / else if statements
    VB:
    If condition Then
        statements
    ElseIf condition Then
        statements
    Else
        statements
    End If
    python:
    if condition:
        statements
    elif condition:
        statements
    else:
        statements
"""
# get an input
number1 = int(input("Enter a number: "))
# get another input
number2 = int(input("Enter another number: "))
# check to see which number is larger or if the numbers are equal
if number1 > number2:
    print(f"{number1} is larger")
elif number2 > number1:
    print(f"{number2} is larger")
else:
    print("Both numbers are equal")