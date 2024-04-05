Attribute VB_Name = "Module1"
Sub Checkerboard():
    'Goal: to make an 8 x 8 checkerboard of alternating black and red cells
    
    ' make a counter to track the cell number
    Dim cellNum As Integer
    cellNum = 1 ' start from 1
    
    ' loop through 8 rows
    For Row = 1 To 8
    
        ' loop through 8 columns on each row
        For Col = 1 To 8
        
            ' if the cell number is even, color the cell black
            If cellNum Mod 2 = 0 Then
                Cells(Row, Col).Interior.ColorIndex = 1
            Else
            
                ' otherwise, color the cell Red
                Cells(Row, Col).Interior.ColorIndex = 3
            End If
            ' increment the count of the cells
            cellNum = cellNum + 1
            
        Next Col
        
        'increment the count of the cell again to shift the coloring of the cells in the next row
        cellNum = cellNum + 1
    Next Row
End Sub
