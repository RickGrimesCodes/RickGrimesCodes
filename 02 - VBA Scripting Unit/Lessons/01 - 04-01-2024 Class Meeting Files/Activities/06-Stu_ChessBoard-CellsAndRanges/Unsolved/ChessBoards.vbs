Attribute VB_Name = "Module2"
Sub ChessBoards():
    'Put the Pawns in place
    Range("A2:H2").Value = "Pawn"
    Range("A7:H7").Value = "Pawn"
    
    'Put the Pawns in place
    Range("A1, H1, A8, H8").Value = "Rook"
    
    'Put the Knights in place
    Range("B1, G1, B8, G8").Value = "Knight"
    
    'Put the Bishops in place
    Range("C1, F1, C8, F8").Value = "Bishops"
    
    'Put the Queens in place
    Range("D1,E8").Value = "Queens"
    
    'Put the Kings in place
    Range("E1,D8").Value = "King"
End Sub
