Attribute VB_Name = "Module1"
Sub ColorFormatter():

    ' to change font color .Font.ColorIndex command
    ' Change the color of the font in Cell A1
    Range("A1").Font.ColorIndex = 3
    
    ' Change the color of the font in Cell B1
    Range("B1").Font.ColorIndex = 4
    
    'Change the color of the font in Cell C1
    Range("C1").Font.ColorIndex = 5
    
    'Change the color of the font in Cell D1
    Range("D1").Font.ColorIndex = 7
    
    ' to change the background color of a cell - .Interior.ColorIndex
    'Change the color of cells A2 - A5
    Range("A2:A5").Interior.ColorIndex = 3
    
    'Change the color of cells B2 - B5
    Range("B2:B5").Interior.ColorIndex = 3
    
    'Change the color of cells C2 - C5
    Range("C2:C5").Interior.ColorIndex = 3
    
    'Change the color of cells D2 - D5
    Range("D2:D5").Interior.ColorIndex = 3
    
    
End Sub
