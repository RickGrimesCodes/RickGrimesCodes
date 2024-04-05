Attribute VB_Name = "Module1"
Sub ArrayDemo():
    Dim ghosts(4) As String ' makes an array of size 4
                            ' each slot in the array happens to have a numerical index
    ' add items to the array
    ghosts(0) = "Inky"
    ghosts(1) = "Blinky"
    ghosts(2) = "Pinky"
    ghosts(3) = "Clyde"
    
    ' display the individual values
    MsgBox (ghosts(0))
    
    Dim phoneNumber As String
    phoneNumber = "704-123-4567"
    
    ' use the SPlit command to split the phone number based on dashes
    Dim phoneNumberArray() As String
    
    phoneNumberArray = Split(phoneNumber, "-")  ' forms a three index array
    
    'display the area code (index 0)
    MsgBox ("Area Code: " & phoneNumberArray(0))
    
    Dim firstLast As String
    firstLast = "Cheesy Mack"
    
    Dim name() As String
    
    name = Split(firstLast, " ") ' split the name based on spaces
    
    MsgBox ("First: " & name(0) & vbCrLf & "Last: " & name(1))
    
End Sub
