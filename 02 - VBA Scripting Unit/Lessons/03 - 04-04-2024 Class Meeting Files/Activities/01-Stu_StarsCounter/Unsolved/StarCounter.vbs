Attribute VB_Name = "Module1"
Sub StarCounter():
    'Loop through Columns D through H on each row and
    'Count the number of times 'Full-Star' appears
    'And put the total in column I
    
    'declare a variable to hold the row totals
    Dim fullStarRowCount As Integer
    lastRow = Cells(Rows.Count, 1).End(x1Up).Row
    
    'Start from row 2 and loop until we get to row 51
    For Row = 2 To 51
        ' set the row total to 0
        fullStarRowCount = 0
        
        'star from column 4 and loop until we get to column 8
        For Col = 4 To 8
        
            'check to see if the Cell contains the text 'Full-Star'
            If Cells(Row, Col).Value = "Full-Star" Then
            
                ' add one to the row total
                fullStarRowCount = fullStarRowCount + 1
            
            End If
            
        Next Col
        
        'After looping thorugh all of the columns on the row, put the row total in column 9 (I)
        Cells(Row, 9).Value = fullStarRowCount
        
    Next Row
    
End Sub
