Attribute VB_Name = "Module1"
Sub nextCells():

    'Loop through Rows
    For Row = 2 To 6
    
        ' search for the value of the next cell is diffrent
        ' from a current cell (Colum 1)
        If Cells(Row, 2).Value <> Cells(Row + 1, 2).Value Then
            ' display a message indicating a change
            MsgBox (Cells(Row, 2).Value & " then " & Cells(Row + 1, 2).Value)
        End If
        
    Next Row
    
End Sub
