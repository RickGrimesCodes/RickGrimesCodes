Attribute VB_Name = "Module1"
Sub CensusDemo():

    For Each ws In Worksheets
    
        ' reference worksheet components by using ws.
            ' ex ws.Cells() or ws.Range()
            
        Dim rowCount As Integer
        rowCount = ws.Cells(Rows.Count, 1).End(xlUp).Row
        
        ' get the name of the worksheet
        Dim worksheetName As String
        
        worksheetName = ws.Name ' .Name gets the text from the tab
        MsgBox (worksheetName)
        
        ' format columns D (4) and E (5)
        For Row = 2 To rowCount
            ws.Cells(Row, 4).Style = "Currency"
            ws.Cells(Row, 5).Style = "Currency"
        Next Row
    ' go to the next worksheet
    Next ws
End Sub
