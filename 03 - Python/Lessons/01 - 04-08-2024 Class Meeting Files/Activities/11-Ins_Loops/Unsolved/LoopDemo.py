"""
    Loops in VB:
    
        For i=1 To 10
            statements
        Next i
        
    loops in Python come in 2 forms:
    
    Condition Controlled - while
        
        while condition:
            statements
           
"""


# variable to control the loop below
number = 5

while loop
    while number > 0:
    print("The number is greater than 0")
     # update the value of number by subtract
     #number = - 1
    number -= 1 # same as number = number - 1
                # can also use with +=, *=, /=, %=
 #use the while loop to check for valid input
 #while number < 1 or number > 5:
   # print("\nERROR: INVALID NUMbER ENTERED. TRY AGAIN")
   # number = int(input("Enter a number between 1 and 5: "))

# while loop that displays the values
# while number > 0:
    # print("The number is greater than 0")
    # number -= 1
"""
 Count Controlled - for
        
        for value in range(num):
            statements
            
        for value in range(start, stop):
            statements
            
        for value in range(start, stop, change):
            statements
    
"""
#start at 2, but go up before 5
#for num in range(2, 5)
    #print(num)
#starts at 2, counts up before 20 in steps of 2
# for num in range(2, 20, 2)
    # print(num)
    

"""
 using for statements with lists and strings
    ghosts = ["Inky", "Blinky", "Pinky", "CLyde"]
    
    for ghosts in ghosts:
        print(ghost)
     
    text = "PYTHON IS FUN!"
    
    for letter in text:
        print(letter)
"""
#ghost = ["Inky", "Blinky", "Pinky", "CLyde"]
    
    #for ghost in ghost:
        #print(ghost)
     
   # text = "PYTHON IS FUN!"
    
   # for letter in text:
        #print(letter)