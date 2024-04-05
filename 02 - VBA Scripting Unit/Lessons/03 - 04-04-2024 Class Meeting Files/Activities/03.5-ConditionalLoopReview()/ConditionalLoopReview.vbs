Attribute VB_Name = "Module1"
Sub conditionalLoopReview()

    For Row = 1 To 5
    
        Cells(Row, 1).Value = Row
        
        ' use Mod to check to see if a row is even or odd
        If Cells(Row, 1).Value Mod 2 = 0 Then
            ' Put even in Colum B
            Cells(Row, 2).Value = "Even"
        Else
            ' Otherwise, put odd in Column B
            Cells(Row, 2).Value = "Odd"
        End If
        
    
    
    Next Row
    
End Sub
