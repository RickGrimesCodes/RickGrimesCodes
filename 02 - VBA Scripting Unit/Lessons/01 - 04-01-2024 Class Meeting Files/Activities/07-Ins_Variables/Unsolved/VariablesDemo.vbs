Attribute VB_Name = "Module1"
Sub VariableDemo():
    'Data in programs can be numerical, text-based, and/or logic-based
    'Numbers can have decimal places (1.51)
    'Numbers can also not have decimal places (10)
        ' Numbers without decimal palces (integers and longs
        
    'to use a variable, declare it first
        'Dim nameOfVariable As DataType
        'to declare an Integer named number:
            Dim number As Integer
         'number is avaiable to use, but has nothing in it
    'then assign the variable a value
        'to store the vbalue of 10 in number:
            number = 10  ' assignment works from right ot left
    'Finally reference the value of the variable by using the variable name
            MsgBox (number) 'display the value of the variable in a message box
            
        'valid variable names: daysOfWeek, numDays, number_of_days
        ' invalid variable names: days of week, 12daysOfWeek
        
    'declare a long integer named bigNumber:
        Dim bigSNumber As Integer
        'bigSNumber = 1000000
    
    ' Number with decimal places are doubles
        Dim numberWithDecimals As Double
        numbersWithDecimals = 15.55
    
    'Text based data in VB is stored as a String
        Dim name As String
        name = "Dr. A"
        
    'declare a variable to hold an age
        Dim age As Integer
        age = 38
    'MsgBox (name)
    'MsgBox (age)
    
    'MsgBox (name + age)
    
    'MsgBox (name + Str(age))
    
    MsgBox (name + Str(age))
    
    MsgBox ("Name: " & name & vbCrLf & "Age: " & age)
    
    'get the value from the cells in our sheet
    Dim firstNUmber As Integer
    Dim secondNumber As Integer
    firstNUmber = Range("B1").Value
    secondNumber = Cells(2, 2).Value
    
    MsgBox ("firstNumber: " & firstNUmber & "secondNumber" & secondNumber)
    
    ' Make a variable to hold the sum / total
    Dim total As Integer
    total = firstNUmber + secondNumber
    
    MsgBox ("total: " & total)
    
    'display the total in the owrksheet
    Range("B3").Value = total
    
End Sub
