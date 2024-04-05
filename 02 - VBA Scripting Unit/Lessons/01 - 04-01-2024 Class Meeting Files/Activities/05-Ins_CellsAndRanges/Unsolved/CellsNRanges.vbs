Attribute VB_Name = "Module1"
Sub CellsNRanges():
    'Cells command
    Cells(1, 1) = "Bootcamp"
    
    'Range command
    Range("A2") = "is fun"
    
    'Range across a row
    Range("A3:C3") = "Code"
    
    'Range down a column
    Range("F1:F3") = "Code Column"
End Sub
