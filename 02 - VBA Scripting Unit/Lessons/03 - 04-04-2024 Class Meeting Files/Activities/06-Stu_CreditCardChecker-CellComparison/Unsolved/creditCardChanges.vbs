Attribute VB_Name = "Module1"
Sub creditCardChanges():
    
    ' declare a variable to hold the row count
    Dim rowCount As Integer
    ' variable to hold the charges for a brand
    Dim brandTotal As Double
    brandTotal = 0 ' start the brand total at 0
    
    ' variable to keep track of changes for the summary data (Columns G and H)
    Dim summaryRow As Integer
    summaryRow = 2 ' starts on row 2 of columns G and H
    
    ' variable to hlld the credit card brand name
    Dim brand As String
    
    ' use x1Up command to get the last row / count of rows
    rowCount = Cells(Rows.Count, "A").End(xlUp).Row
    
    ' Loop through Column A and check to see where we have changes
    For Row = 2 To rowCount
    
        ' simply track changes
        If Cells(Row, 1).Value <> Cells(Row + 1, 1).Value Then
            ' if the card brand changes, do the following:
            brand = Cells(Row, 1).Value
            
            ' add on to the brand total one last time
            brandTotal = brandTotal + Cells(Row, 3).Value
            
            ' display the changed brand in Column G
            Cells(summaryRow, 7).Value = brand
            
            ' display the total of the brand's charges in column H
            Cells(summaryRow, 8).Value = brandTotal
            
            ' reset the brandTotal
            brandTotal = 0
            
            'add  one onto the summary row for next credit card brand
            summaryRow = summaryRow + 1
        
        Else
            ' add on to the total of the brand's charges
            ' add on to the total of the brand's charges
            brandTotal = brandTotal + Cells(Row, 3).Value
            
            
        End If
    Next Row
    
End Sub
