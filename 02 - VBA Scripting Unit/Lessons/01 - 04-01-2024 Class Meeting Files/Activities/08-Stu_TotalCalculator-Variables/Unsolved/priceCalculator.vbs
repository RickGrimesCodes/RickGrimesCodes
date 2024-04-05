Attribute VB_Name = "Module2"
Sub priceCalculator():
    ' variables to hold the itemPrice, taxRate, qty, and total
    Dim itemPrice As Double
    Dim taxRate As Double
    Dim qty As Double
    Dim total As Double
    
    ' get the values from Row 2 and store in the price, tax, and quantity variable
    itemPrice = Range("B2").Value
    taxRate = Range("C2").Value
    qty = Range("D2").Value
    
    ' calculate the total
    total = itemPrice * (1 + taxRate) * qty
    
    'put the total in cell E2
    Range("E2").Value = total
    
    ' display the message box
    MsgBox ("Your otal is $" & total)
    
End Sub
